"""
classifier_v2_stress_test.py

Stress-test NutriHelp Classifier V2 on challenging images:
- blur
- low light
- side angle
- cluttered background
- multi-food

This script loads the trained MobileNetV2 model and runs inference
without retraining.
"""

import os
import torch
from torchvision import transforms, models
from PIL import Image

# -----------------------------
# Configuration
# -----------------------------
MODEL_PATH = "models/classifier_v2_mobilenet_best.pth"
STRESS_ROOT = "stress_test_images"
IMG_SIZE = 224

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {DEVICE}")

# Class labels (must match training order)
CLASS_NAMES = [
    'beef', 'bread', 'chicken', 'egg', 'fruit',
    'lamb', 'noodles', 'pasta', 'pork', 'rice',
    'salad', 'seafood', 'snacks', 'soup', 'vegetables'
]

# -----------------------------
# Image transforms
# -----------------------------
transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])

# -----------------------------
# Load model
# -----------------------------
def load_model():
    weights = models.MobileNet_V2_Weights.DEFAULT
    model = models.mobilenet_v2(weights=weights)

    in_features = model.classifier[1].in_features
    model.classifier[1] = torch.nn.Linear(in_features, len(CLASS_NAMES))

    model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    model.to(DEVICE)
    model.eval()
    return model

model = load_model()
print("Model loaded successfully.")

# -----------------------------
# Inference helper
# -----------------------------
def predict_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        outputs = model(image)
        probs = torch.softmax(outputs, dim=1)
        confidence, pred_idx = torch.max(probs, 1)

    return CLASS_NAMES[pred_idx.item()], confidence.item()

# -----------------------------
# Stress testing loop
# -----------------------------
results = []

print("\nStarting stress test...\n")

for category in os.listdir(STRESS_ROOT):
    category_path = os.path.join(STRESS_ROOT, category)

    if not os.path.isdir(category_path):
        continue

    print(f"Category: {category}")
    results.append(f"\n=== {category.upper()} ===")

    for img_name in os.listdir(category_path):
        img_path = os.path.join(category_path, img_name)

        pred_class, conf = predict_image(img_path)

        line = f"{img_name:25s} -> {pred_class:12s} | confidence: {conf:.2f}"
        print(line)
        results.append(line)

# -----------------------------
# Save results
# -----------------------------
output_file = "models/classifier_v2_stress_test_results.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(results))

print(f"\nStress test results saved to {output_file}")
print("Done.")