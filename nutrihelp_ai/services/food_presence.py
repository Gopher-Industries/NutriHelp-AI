from __future__ import annotations

import logging
from io import BytesIO
from pathlib import Path
from typing import Dict, Optional

import numpy as np
from PIL import Image, ImageFilter, ImageOps, ImageStat

try:
    import joblib
except Exception:  # pragma: no cover - joblib is expected with scikit-learn.
    joblib = None


logger = logging.getLogger(__name__)

MODEL_PATH = Path(__file__).resolve().parents[2] / "models" / "food_presence_model.joblib"
DEFAULT_FOOD_THRESHOLD = 0.45


def _histogram(values: np.ndarray, bins: int, value_range: tuple[float, float]) -> np.ndarray:
    hist, _ = np.histogram(values, bins=bins, range=value_range)
    total = max(1, int(hist.sum()))
    return hist.astype(np.float32) / float(total)


def extract_food_presence_features(image: Image.Image) -> np.ndarray:
    image = ImageOps.exif_transpose(image).convert("RGB")
    width, height = image.size
    resized = image.resize((128, 128))
    rgb = np.asarray(resized, dtype=np.float32) / 255.0
    gray = np.asarray(resized.convert("L"), dtype=np.float32) / 255.0
    hsv = np.asarray(resized.convert("HSV"), dtype=np.float32)

    edge_image = resized.convert("L").filter(ImageFilter.FIND_EDGES)
    edge_values = np.asarray(edge_image, dtype=np.float32) / 255.0
    stat = ImageStat.Stat(resized.convert("L"))

    features = [
        width / max(1, height),
        min(width, height) / max(1, max(width, height)),
        float(stat.mean[0]) / 255.0,
        float(stat.stddev[0]) / 255.0,
        float(edge_values.mean()),
        float(np.mean(edge_values > 0.18)),
        float(rgb.mean()),
        float(rgb.std()),
        float(hsv[:, :, 1].mean()) / 255.0,
        float(hsv[:, :, 1].std()) / 255.0,
        float(hsv[:, :, 2].mean()) / 255.0,
        float(hsv[:, :, 2].std()) / 255.0,
    ]

    for channel in range(3):
        values = rgb[:, :, channel].reshape(-1)
        features.extend(
            [
                float(values.mean()),
                float(values.std()),
                float(np.percentile(values, 10)),
                float(np.percentile(values, 50)),
                float(np.percentile(values, 90)),
            ]
        )

    features.extend(_histogram(gray.reshape(-1), bins=16, value_range=(0.0, 1.0)))
    features.extend(_histogram(hsv[:, :, 0].reshape(-1), bins=16, value_range=(0.0, 255.0)))
    features.extend(_histogram(hsv[:, :, 1].reshape(-1), bins=16, value_range=(0.0, 255.0)))
    features.extend(_histogram(edge_values.reshape(-1), bins=8, value_range=(0.0, 1.0)))

    return np.asarray(features, dtype=np.float32)


class FoodPresenceService:
    def __init__(
        self,
        model_path: Path | str = MODEL_PATH,
        threshold: float = DEFAULT_FOOD_THRESHOLD,
    ):
        self.model_path = Path(model_path)
        self.threshold = float(threshold)
        self._model = None
        self._load_error: Optional[str] = None

    def _get_model(self):
        if self._model is not None:
            return self._model
        if self._load_error is not None:
            return None
        if joblib is None:
            self._load_error = "joblib is unavailable"
            logger.warning("Food presence model disabled: %s", self._load_error)
            return None
        if not self.model_path.exists():
            self._load_error = f"model not found at {self.model_path}"
            logger.info("Food presence model disabled: %s", self._load_error)
            return None

        try:
            payload = joblib.load(self.model_path)
            self._model = payload.get("model", payload) if isinstance(payload, dict) else payload
            if isinstance(payload, dict) and "threshold" in payload:
                self.threshold = float(payload["threshold"])
            return self._model
        except Exception as exc:
            self._load_error = str(exc)
            logger.warning("Food presence model disabled: %s", exc, exc_info=True)
            return None

    def analyze(self, image_bytes: bytes) -> Dict[str, object]:
        model = self._get_model()
        if model is None:
            return {
                "enabled": False,
                "is_food": True,
                "food_probability": 1.0,
                "threshold": self.threshold,
                "reason": self._load_error or "model unavailable",
            }

        with Image.open(BytesIO(image_bytes)) as src:
            features = extract_food_presence_features(src).reshape(1, -1)

        if hasattr(model, "predict_proba"):
            probability = float(model.predict_proba(features)[0][1])
        else:
            probability = float(model.predict(features)[0])

        is_food = probability >= self.threshold
        return {
            "enabled": True,
            "is_food": is_food,
            "food_probability": round(probability, 4),
            "threshold": self.threshold,
            "reason": ""
            if is_food
            else f"Image does not appear to contain food; food probability {probability:.2f} below {self.threshold:.2f}.",
        }
