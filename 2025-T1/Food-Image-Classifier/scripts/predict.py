import torch
from torchvision import transforms
from torchvision.datasets import Food101
from PIL import Image
import json
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

def predict_image(image_path):
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        outputs = model(image)
        probs = torch.softmax(outputs, dim=1)
        top_prob, top_class = torch.max(probs, 1)

    food_name = CLASS_NAMES[top_class.item()]

    result = {
        "predicted_class": food_name,
        "confidence": round(top_prob.item(), 4)
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
