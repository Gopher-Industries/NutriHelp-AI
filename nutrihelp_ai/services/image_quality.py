from io import BytesIO
from typing import Dict, List, Optional

import numpy as np
from PIL import Image, ImageFilter, ImageOps, ImageStat, UnidentifiedImageError

try:
    import cv2
except Exception:  # pragma: no cover - OpenCV may be unavailable in minimal envs.
    cv2 = None


MIN_DIMENSION = 160
MIN_BRIGHTNESS = 35.0
MAX_BRIGHTNESS = 235.0
MIN_CONTRAST = 18.0
MIN_SHARPNESS = 10.0
MAX_FACE_AREA_RATIO = 0.22
PEOPLE_DETECTION_MIN_RATIO = 0.045
SCREENSHOT_EDGE_RATIO = 0.18
SCREENSHOT_LOW_SATURATION_RATIO = 0.45
CARTOON_FLAT_REGION_RATIO = 0.58
CARTOON_EDGE_RATIO = 0.08
CARTOON_SATURATION_MIN = 45.0


class InvalidImageError(ValueError):
    pass


class ImageQualityService:
    def _edge_ratio(self, gray_array: np.ndarray) -> float:
        if cv2 is not None:
            edges = cv2.Canny(gray_array.astype(np.uint8), 80, 180)
            return float(np.mean(edges > 0))

        gy, gx = np.gradient(gray_array.astype(float))
        magnitude = np.sqrt(gx * gx + gy * gy)
        return float(np.mean(magnitude > 35.0))

    def _looks_like_screenshot(self, image: Image.Image, gray_array: np.ndarray) -> bool:
        width, height = image.size
        if width < 300 or height < 300:
            return False

        edge_ratio = self._edge_ratio(gray_array)
        hsv = image.convert("HSV")
        saturation = np.array(hsv, dtype=np.uint8)[:, :, 1]
        value = np.array(hsv, dtype=np.uint8)[:, :, 2]
        low_saturation_ratio = float(np.mean(saturation < 35))
        high_value_ratio = float(np.mean(value > 225))
        dark_value_ratio = float(np.mean(value < 35))

        return (
            edge_ratio >= SCREENSHOT_EDGE_RATIO
            and low_saturation_ratio >= SCREENSHOT_LOW_SATURATION_RATIO
            and (high_value_ratio >= 0.18 or dark_value_ratio >= 0.18)
        )

    def _looks_like_cartoon_or_portrait(self, image: Image.Image, gray_array: np.ndarray) -> bool:
        width, height = image.size
        if width < 180 or height < 180:
            return False

        small = image.resize((96, 96))
        rgb = np.array(small, dtype=np.int16)
        horizontal_diff = np.abs(np.diff(rgb, axis=1)).mean(axis=2)
        vertical_diff = np.abs(np.diff(rgb, axis=0)).mean(axis=2)
        flat_ratio = float(
            (
                np.mean(horizontal_diff < 8.0)
                + np.mean(vertical_diff < 8.0)
            )
            / 2.0
        )
        edge_ratio = self._edge_ratio(gray_array)
        saturation_mean = float(np.array(image.convert("HSV"), dtype=np.uint8)[:, :, 1].mean())

        return (
            flat_ratio >= CARTOON_FLAT_REGION_RATIO
            and edge_ratio <= CARTOON_EDGE_RATIO
            and saturation_mean >= CARTOON_SATURATION_MIN
        )

    def _contains_large_face(self, image: Image.Image) -> bool:
        if cv2 is None:
            return False

        cascade_path = getattr(cv2.data, "haarcascades", "") + "haarcascade_frontalface_default.xml"
        classifier = cv2.CascadeClassifier(cascade_path)
        if classifier.empty():
            return False

        rgb = np.array(image)
        gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
        faces = classifier.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=7,
            minSize=(90, 90),
        )
        if len(faces) == 0:
            return False

        image_area = max(1, image.size[0] * image.size[1])
        largest_face_area = max(int(width) * int(height) for _, _, width, height in faces)
        return (largest_face_area / image_area) >= MAX_FACE_AREA_RATIO

    def _contains_people_scene(self, image: Image.Image) -> bool:
        if cv2 is None:
            return False

        rgb = np.array(image)
        gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
        image_area = max(1, image.size[0] * image.size[1])
        cascade_names = [
            "haarcascade_frontalface_default.xml",
            "haarcascade_profileface.xml",
            "haarcascade_upperbody.xml",
            "haarcascade_fullbody.xml",
        ]

        for cascade_name in cascade_names:
            cascade_path = getattr(cv2.data, "haarcascades", "") + cascade_name
            classifier = cv2.CascadeClassifier(cascade_path)
            if classifier.empty():
                continue

            detections = classifier.detectMultiScale(
                gray,
                scaleFactor=1.08,
                minNeighbors=5,
                minSize=(48, 48),
            )
            if len(detections) == 0:
                continue

            largest_area = max(int(width) * int(height) for _, _, width, height in detections)
            if (largest_area / image_area) >= PEOPLE_DETECTION_MIN_RATIO:
                return True

        return False

    def analyze(self, image_bytes: bytes) -> Dict[str, object]:
        if not image_bytes:
            raise InvalidImageError("Uploaded file is empty.")

        try:
            with Image.open(BytesIO(image_bytes)) as src:
                image = ImageOps.exif_transpose(src).convert("RGB")
        except UnidentifiedImageError as exc:
            raise InvalidImageError("Uploaded file is not a supported image.") from exc

        width, height = image.size
        gray = image.convert("L")
        gray_array = np.array(gray, dtype=np.uint8)
        brightness = round(float(ImageStat.Stat(gray).mean[0]), 2)
        contrast = round(float(ImageStat.Stat(gray).stddev[0]), 2)
        edges = gray.filter(ImageFilter.FIND_EDGES)
        sharpness = round(float(ImageStat.Stat(edges).mean[0]), 2)
        contains_large_face = self._contains_large_face(image)
        contains_people_scene = self._contains_people_scene(image)
        looks_like_screenshot = self._looks_like_screenshot(image, gray_array)
        looks_like_cartoon_or_portrait = self._looks_like_cartoon_or_portrait(image, gray_array)

        issues: List[str] = []
        if min(width, height) < MIN_DIMENSION:
            issues.append(f"Image resolution is too low. Minimum side is {MIN_DIMENSION}px.")
        if brightness < MIN_BRIGHTNESS:
            issues.append("Image is too dark.")
        elif brightness > MAX_BRIGHTNESS:
            issues.append("Image is too bright.")
        if contrast < MIN_CONTRAST:
            issues.append("Image has low contrast.")
        if sharpness < MIN_SHARPNESS:
            issues.append("Image appears blurry.")
        if contains_large_face:
            issues.append("Image appears to contain a large face. Please upload a clear food photo.")
        if looks_like_screenshot:
            issues.append("Image appears to be a screenshot or interface, not a clear food photo.")
        if looks_like_cartoon_or_portrait:
            issues.append("Image appears to be an illustration or portrait, not a clear food photo.")

        blocking_quality_issue = (
            min(width, height) < MIN_DIMENSION
            or sharpness < MIN_SHARPNESS
            or looks_like_screenshot
        )

        return {
            "width": width,
            "height": height,
            "brightness": brightness,
            "contrast": contrast,
            "sharpness": sharpness,
            "passed": not blocking_quality_issue,
            "issues": issues,
            "should_mark_unclear": blocking_quality_issue,
            "should_reject_prediction": looks_like_screenshot,
            "contains_people_scene": contains_people_scene,
        }

    def response_payload(self, analysis: Dict[str, object]) -> Dict[str, object]:
        return {
            "width": int(analysis.get("width", 0)),
            "height": int(analysis.get("height", 0)),
            "brightness": float(analysis.get("brightness", 0.0)),
            "contrast": float(analysis.get("contrast", 0.0)),
            "sharpness": float(analysis.get("sharpness", 0.0)),
            "passed": bool(analysis.get("passed", False)),
            "issues": list(analysis.get("issues", [])),
        }

    def fallback_payload(self, issues: Optional[List[str]] = None) -> Dict[str, object]:
        return {
            "width": 0,
            "height": 0,
            "brightness": 0.0,
            "contrast": 0.0,
            "sharpness": 0.0,
            "passed": False,
            "issues": list(issues or []),
        }
