from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable

import joblib
import numpy as np
from PIL import Image, UnidentifiedImageError
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from nutrihelp_ai.services.food_presence import extract_food_presence_features


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
SPLIT_NAMES = {
    "training": "train",
    "validation": "validation",
    "evaluation": "test",
}


def iter_images(folder: Path) -> Iterable[Path]:
    for path in sorted(folder.rglob("*")):
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
            yield path


def load_split(dataset_dir: Path, split: str) -> tuple[np.ndarray, np.ndarray]:
    rows = []
    labels = []
    split_dir = dataset_dir / split
    for class_name, label in [("non_food", 0), ("food", 1)]:
        class_dir = split_dir / class_name
        if not class_dir.is_dir():
            raise FileNotFoundError(f"Missing expected folder: {class_dir}")
        for image_path in iter_images(class_dir):
            try:
                with Image.open(image_path) as image:
                    rows.append(extract_food_presence_features(image))
                labels.append(label)
            except (UnidentifiedImageError, OSError) as exc:
                print(f"Skipping unreadable image {image_path}: {exc}")
    if not rows:
        raise RuntimeError(f"No images found for split {split_dir}")
    return np.vstack(rows), np.asarray(labels, dtype=np.int64)


def evaluate(name: str, model, x: np.ndarray, y: np.ndarray) -> dict[str, float]:
    predicted = model.predict(x)
    probabilities = model.predict_proba(x)[:, 1]
    accuracy = accuracy_score(y, predicted)
    auc = roc_auc_score(y, probabilities)
    print(f"\n{name} accuracy: {accuracy:.4f}")
    print(f"{name} ROC-AUC: {auc:.4f}")
    print(f"{name} confusion matrix [non_food, food]:")
    print(confusion_matrix(y, predicted))
    print(classification_report(y, predicted, target_names=["non_food", "food"]))
    return {"accuracy": float(accuracy), "roc_auc": float(auc)}


def main() -> None:
    parser = argparse.ArgumentParser(description="Train Food-5K food/non-food gate.")
    parser.add_argument(
        "--dataset-dir",
        default="nutrihelp_ai/data/food5k",
        help="Path containing Food-5K training/validation/evaluation folders.",
    )
    parser.add_argument(
        "--output",
        default="models/food_presence_model.joblib",
        help="Where to save the trained model.",
    )
    parser.add_argument("--threshold", type=float, default=0.45)
    parser.add_argument("--trees", type=int, default=400)
    args = parser.parse_args()

    dataset_dir = Path(args.dataset_dir)
    output_path = Path(args.output)

    datasets = {}
    for split in SPLIT_NAMES:
        print(f"Loading {split}...")
        datasets[split] = load_split(dataset_dir, split)
        print(f"{split}: {datasets[split][0].shape[0]} images")

    model = ExtraTreesClassifier(
        n_estimators=args.trees,
        random_state=42,
        class_weight="balanced",
        n_jobs=-1,
        min_samples_leaf=2,
    )

    x_train, y_train = datasets["training"]
    model.fit(x_train, y_train)

    metrics = {}
    for source_split, metric_name in SPLIT_NAMES.items():
        metrics[metric_name] = evaluate(metric_name, model, *datasets[source_split])

    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(
        {
            "model": model,
            "threshold": args.threshold,
            "metrics": metrics,
            "feature_count": int(x_train.shape[1]),
            "classes": ["non_food", "food"],
            "dataset": "Food-5K",
        },
        output_path,
    )
    print(f"\nSaved model to {output_path}")


if __name__ == "__main__":
    main()
