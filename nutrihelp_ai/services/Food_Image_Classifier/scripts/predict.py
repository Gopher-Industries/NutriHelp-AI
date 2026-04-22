import io
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

import torch
from PIL import Image

try:
    from .augment import build_eval_transform
    from .model import FoodClassifier
except ImportError:  # pragma: no cover - script execution fallback
    from augment import build_eval_transform
    from model import FoodClassifier


DEFAULT_IMAGE_SIZE = 224
DEFAULT_NORMALIZATION = "legacy_half"
TOPK_DEFAULT = 5
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MODEL_PATH = Path(__file__).resolve().parent.parent / "outputs" / "models" / "food_classifier.pth"
CLASSES_PATH = Path(__file__).resolve().parent / "classes.json"


class Predictor:
    def __init__(
        self,
        model_path: Optional[str] = None,
        classes_path: Optional[str] = None,
        device: Optional[str] = None,
    ):
        self.device = torch.device(device) if device else DEVICE
        self.model_path = Path(model_path) if model_path else MODEL_PATH
        self.classes_path = Path(classes_path) if classes_path else CLASSES_PATH

        checkpoint = torch.load(str(self.model_path), map_location=self.device)
        self.metadata = (
            checkpoint
            if isinstance(checkpoint, dict)
            and any(
                key in checkpoint
                for key in ("model_state", "state_dict", "model", "image_size", "classes", "normalization")
            )
            else {}
        )

        if isinstance(self.metadata.get("classes"), list):
            self.class_names = list(self.metadata["classes"])
        else:
            with open(self.classes_path, "r") as f:
                self.class_names = json.load(f)

        image_size = self.metadata.get("image_size", DEFAULT_IMAGE_SIZE)
        if isinstance(image_size, (list, tuple)):
            image_size = image_size[0]
        self.image_size = int(image_size)
        self.normalization = self.metadata.get("normalization", DEFAULT_NORMALIZATION)

        model_state = (
            self.metadata.get("model_state")
            or self.metadata.get("state_dict")
            or self.metadata.get("model")
            or checkpoint
        )

        self.model = FoodClassifier(
            num_classes=len(self.class_names),
            use_pretrained=False,
        )
        self.model.load_state_dict(model_state)
        self.model.to(self.device).eval()
        self.transform = build_eval_transform(
            image_size=self.image_size,
            normalization=self.normalization,
        )

    def _pil_from_bytes(self, image_bytes: bytes) -> Image.Image:
        return Image.open(io.BytesIO(image_bytes)).convert("RGB")

    @torch.no_grad()
    def _predict_pil(self, image: Image.Image, topk: int = TOPK_DEFAULT) -> Dict[str, Any]:
        tensor = self.transform(image).unsqueeze(0).to(self.device)
        outputs = self.model(tensor)
        probabilities = torch.softmax(outputs, dim=1).cpu().squeeze(0)

        safe_topk = max(1, min(int(topk), len(self.class_names)))
        top_scores, top_indices = torch.topk(probabilities, k=safe_topk)
        topk_items: List[Dict[str, Any]] = [
            {
                "label": self.class_names[index],
                "score": round(float(score), 4),
            }
            for score, index in zip(top_scores.tolist(), top_indices.tolist())
        ]

        best = topk_items[0] if topk_items else {"label": None, "score": 0.0}
        return {
            "label": best["label"],
            "confidence": float(best["score"]),
            "topk": topk_items,
        }

    def predict_from_bytes(self, image_bytes: bytes, topk: int = TOPK_DEFAULT) -> Dict[str, Any]:
        return self._predict_pil(self._pil_from_bytes(image_bytes), topk=topk)

    def predict_path(self, image_path: str, topk: int = TOPK_DEFAULT) -> Dict[str, Any]:
        return self._predict_pil(Image.open(image_path).convert("RGB"), topk=topk)


_predictor: Optional[Predictor] = None


def get_predictor() -> Predictor:
    global _predictor
    if _predictor is None:
        _predictor = Predictor()
    return _predictor


def predict_image(image_path: str, topk: int = TOPK_DEFAULT) -> Dict[str, Any]:
    result = get_predictor().predict_path(image_path, topk=topk)
    return {
        "predicted_class": result["label"],
        "confidence": round(result["confidence"], 4),
        "topk": result["topk"],
    }


def predict_bytes(image_bytes: bytes, topk: int = TOPK_DEFAULT) -> Dict[str, Any]:
    return get_predictor().predict_from_bytes(image_bytes, topk=topk)


if __name__ == "__main__":
    test_image_path = Path(__file__).resolve().parent / "sample.jpg"
    print(json.dumps(predict_image(str(test_image_path)), indent=2))
