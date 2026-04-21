from io import BytesIO
from typing import Dict, List, Optional

from PIL import Image, ImageFilter, ImageOps, ImageStat, UnidentifiedImageError


MIN_DIMENSION = 160
MIN_BRIGHTNESS = 35.0
MAX_BRIGHTNESS = 235.0
MIN_CONTRAST = 18.0
MIN_SHARPNESS = 10.0


class InvalidImageError(ValueError):
    pass


class ImageQualityService:
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
        brightness = round(float(ImageStat.Stat(gray).mean[0]), 2)
        contrast = round(float(ImageStat.Stat(gray).stddev[0]), 2)
        edges = gray.filter(ImageFilter.FIND_EDGES)
        sharpness = round(float(ImageStat.Stat(edges).mean[0]), 2)

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

        should_mark_unclear = (
            min(width, height) < MIN_DIMENSION
            or sharpness < MIN_SHARPNESS
            or len(issues) >= 2
        )

        return {
            "width": width,
            "height": height,
            "brightness": brightness,
            "contrast": contrast,
            "sharpness": sharpness,
            "passed": len(issues) == 0,
            "issues": issues,
            "should_mark_unclear": should_mark_unclear,
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
