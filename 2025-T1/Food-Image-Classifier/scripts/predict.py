import torch
from torchvision import transforms
from torchvision.datasets import Food101
from PIL import Image
import json
import numpy as np
import os

from model import FoodClassifier

NUM_CLASSES = 101
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
MODEL_PATH = '../outputs/models/food_classifier.pth'
IMAGE_SIZE = (224, 224)

#CLASS_NAMES = Food101(root='data', download=True).classes  
with open("classes.json", "r") as f:
    CLASS_NAMES = json.load(f)  

transform = transforms.Compose([
    transforms.Resize(IMAGE_SIZE),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5]*3, std=[0.5]*3)
])

model = FoodClassifier(num_classes=NUM_CLASSES)
model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
model.to(DEVICE)
model.eval()

def get_confidence_tier(confidence):
    if confidence >= 0.75:
        return "high"
    elif confidence >= 0.50:
        return "medium"
    else:
        return "low"

def check_image_quality(image_path):
    try:
        image = Image.open(image_path).convert('RGB')
    except Exception as e:
        return {"is_low_quality": True, "issues": [f"could not open image: {e}"]}
        
    width, height = image.size
    gray = image.convert('L')
    gray_array = np.array(gray, dtype=float)
    gy, gx = np.gradient(gray_array)
    laplacian_var = np.var(gx + gy)
    is_blurry = laplacian_var < 40  # lowered — phone photos score ~49
    brightness = np.mean(gray_array)
    is_too_dark = brightness < 40
    is_too_bright = brightness > 220
    is_too_small = width < 100 or height < 100

    issues = []
    if is_blurry:
        issues.append("image is blurry")
    if is_too_dark:
        issues.append("image is too dark")
    if is_too_bright:
        issues.append("image is too bright/washed out")
    if is_too_small:
        issues.append("image resolution is too low")

    return {
        "is_low_quality": len(issues) > 0,
        "issues": issues
    }

def predict_image(image_path):
    quality = check_image_quality(image_path)
    if quality["is_low_quality"]:
        return {
            "retake_needed": True,
            "reason": "Please retake the image: " + ", ".join(quality["issues"]),
            "predicted_class": None,
            "confidence": None,
            "confidence_tier": None,
            "top3_predictions": []
        }
        
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        outputs = model(image)
        probs = torch.softmax(outputs, dim=1)
        # top_prob, top_class = torch.max(probs, 1)

    top3_probs, top3_classes = torch.topk(probs, 3, dim=1)
    top3 = [
        {"class": CLASS_NAMES[top3_classes[0][i].item()],
         "confidence": round(top3_probs[0][i].item(), 4)}
        for i in range(3)
    ]

    best = top3[0]

    result = {
        "retake_needed":    False,
        "reason":           None,
        "predicted_class":  best["class"],
        "confidence":       best["confidence"],
        "confidence_tier":  get_confidence_tier(best["confidence"]),
        "top3_predictions": top3
    }

    return result

#Example
if __name__ == "__main__":
    test_image_path = "sample.jpg"  
    result = predict_image(test_image_path)
    print(json.dumps(result, indent=2))

    test_image_path1 = "sample1.jpg"  
    result1 = predict_image(test_image_path1)
    print(json.dumps(result1, indent=2))
