import torch
from torchvision import transforms

# Load model if you have one
# model = torch.load("nutrihelp_ai/models/resnet50d.pth")
# model.eval()


def transform_image(image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)


def predict_image_service(image):
    tensor = transform_image(image)
    # with torch.no_grad():
    #     outputs = model(tensor)
    #     predicted = outputs.argmax(1).item()
    return {
        "prediction": "dummy_class",
        "confidence": 0.99
    }
