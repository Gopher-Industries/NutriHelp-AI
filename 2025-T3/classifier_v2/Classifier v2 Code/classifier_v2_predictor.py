# classifier_v2_predictor.py
# Interactive predictor for classifier v2 (MobileNetV2 + state_dict)
# - Loads state_dict from models/classifier_v2_mobilenet_best.pth
# - Shows Top-3 predictions with confidence
# - Adds "unclear image" logic using a confidence threshold

import os
import sys
from typing import List, Tuple

import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

# -----------------------------
# CONFIG
# -----------------------------
MODEL_PATH = os.path.join("models", "classifier_v2_mobilenet_best.pth")
NUM_CLASSES = 15

# IMPORTANT: Replace these with your real 15 class names (IN THE SAME ORDER used during training).
# Example placeholders only:
CLASS_NAMES = [
    'beef', 'bread', 'chicken', 'egg', 'fruit',
    'lamb', 'noodles', 'pasta', 'pork', 'rice',
    'salad', 'seafood', 'snacks', 'soup', 'vegetables'
]

# If top-1 confidence < this value => mark as "UNCLEAR IMAGE"
UNCLEAR_THRESHOLD = 0.35

# -----------------------------
# TRANSFORMS (must match training as closely as possible)
# -----------------------------
# If your training used different normalization, update mean/std accordingly.
# These are ImageNet defaults (common for MobileNetV2 fine-tuning).
IMG_SIZE = 224
TRANSFORM = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

# -----------------------------
# MODEL LOADING
# -----------------------------
def build_mobilenet_v2(num_classes: int) -> nn.Module:
    """Create MobileNetV2 and replace classifier head for num_classes."""
    model = models.mobilenet_v2(pretrained=False)
    in_features = model.classifier[1].in_features
    model.classifier[1] = nn.Linear(in_features, num_classes)
    return model


def load_model(model_path: str, device: torch.device, num_classes: int) -> nn.Module:
    """Load a state_dict checkpoint into a rebuilt model architecture."""
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Model file not found: {model_path}\n"
            f"Tip: make sure you're running from the repo root and the model is inside /models."
        )

    model = build_mobilenet_v2(num_classes)

    state_dict = torch.load(model_path, map_location=device)
    if not isinstance(state_dict, dict):
        raise ValueError(
            "Loaded checkpoint is not a state_dict dict. "
            "If you saved the full model, you should use torch.load(model_path) directly."
        )

    # Load weights
    model.load_state_dict(state_dict)
    model.to(device)
    model.eval()
    return model


# -----------------------------
# PREDICTION
# -----------------------------
@torch.no_grad()
def predict_image(
    model: nn.Module,
    image_path: str,
    device: torch.device,
    class_names: List[str],
    topk: int = 3
) -> List[Tuple[str, float]]:
    """Return list of (class_name, confidence) sorted high->low."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    # Load & convert to RGB
    img = Image.open(image_path).convert("RGB")
    x = TRANSFORM(img).unsqueeze(0).to(device)  # [1, 3, 224, 224]

    logits = model(x)
    probs = torch.softmax(logits, dim=1).squeeze(0)  # [C]

    topk = min(topk, probs.shape[0])
    confs, idxs = torch.topk(probs, k=topk)

    results: List[Tuple[str, float]] = []
    for conf, idx in zip(confs.tolist(), idxs.tolist()):
        label = class_names[idx] if idx < len(class_names) else f"class_{idx}"
        results.append((label, float(conf)))
    return results


def format_results(results: List[Tuple[str, float]]) -> str:
    return " | ".join([f"{name}: {conf:.2f}" for name, conf in results])


# -----------------------------
# MAIN (Interactive CLI)
# -----------------------------
def main():
    if len(CLASS_NAMES) != NUM_CLASSES:
        print(
            f"[WARNING] CLASS_NAMES has {len(CLASS_NAMES)} items but NUM_CLASSES = {NUM_CLASSES}.\n"
            f"Please update CLASS_NAMES to exactly {NUM_CLASSES} class names in the correct training order.\n"
        )

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    try:
        model = load_model(MODEL_PATH, device, NUM_CLASSES)
        print("Model loaded successfully.\n")
    except Exception as e:
        print(f"[ERROR] Failed to load model: {e}")
        sys.exit(1)

    print("Interactive Mode")
    print("- Paste an image path and press Enter")
    print("- Or type: exit")
    print("- Optional: type 'threshold 0.40' to change unclear threshold\n")

    global UNCLEAR_THRESHOLD

    while True:
        user_input = input("Enter an image path (or command): ").strip()

        if user_input == "":
            # allow blank to keep going instead of exit (more user-friendly)
            print("(Tip: type 'exit' to quit)\n")
            continue

        if user_input.lower() in {"exit", "quit", "q"}:
            print("Exiting.")
            break

        # Change threshold command
        if user_input.lower().startswith("threshold"):
            parts = user_input.split()
            if len(parts) == 2:
                try:
                    new_t = float(parts[1])
                    if 0.0 < new_t < 1.0:
                        UNCLEAR_THRESHOLD = new_t
                        print(f"Unclear threshold set to {UNCLEAR_THRESHOLD:.2f}\n")
                    else:
                        print("Threshold must be between 0 and 1.\n")
                except ValueError:
                    print("Invalid threshold value. Example: threshold 0.35\n")
            else:
                print("Usage: threshold 0.35\n")
            continue

        # Predict
        image_path = user_input.strip('"').strip("'")  # handle pasted quotes

        try:
            results = predict_image(model, image_path, device, CLASS_NAMES, topk=3)
            top1_label, top1_conf = results[0]

            # Unclear logic
            if top1_conf < UNCLEAR_THRESHOLD:
                print(f"[UNCLEAR IMAGE] Top-1 confidence {top1_conf:.2f} < {UNCLEAR_THRESHOLD:.2f}")
                print(f"Top-3 => {format_results(results)}\n")
            else:
                print(f"Prediction: {top1_label}  | confidence: {top1_conf:.2f}")
                print(f"Top-3 => {format_results(results)}\n")

        except Exception as e:
            print(f"[ERROR] {e}\n")


if __name__ == "__main__":
    main()