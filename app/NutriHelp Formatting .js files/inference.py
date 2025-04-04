import torch
from torchvision import transforms
from PIL import Image

# (Optional) import your custom model class if needed
# from train import SELFMODEL

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 1) Load Model
# If you have a custom SELFMODEL, use that. Otherwise, for example:
# model = SELFMODEL(model_name="resnet50d", out_features=101, pretrained=False)

model_path = "../models/resnet50d_14epochs_accuracy0.99144_weights.pth"  # Path to your trained model weights. Ask a member to receive this file and put it in the target directory
# model.load_state_dict(torch.load(model_path, map_location=device))
# model.eval()
# model.to(device)

# For demonstration, let's assume "model" is loaded. 
# If you don’t have a real model, comment out the lines above.

# 2) Define image transforms
def transform_image(image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406], 
            std=[0.229, 0.224, 0.225]
        )
    ])
    return transform(image).unsqueeze(0)

# 3) Prediction function
def predict_image(image):
    """Receives a PIL image, returns JSON of predicted class & confidence."""
    
    # Transform the image
    tensor = transform_image(image).to(device)

    # Inference
    # with torch.no_grad():
    #     output = model(tensor)
    #     probs = torch.nn.functional.softmax(output[0], dim=0)
    #     predicted_idx = torch.argmax(probs).item()
    #     confidence = probs[predicted_idx].item()
    
    # Dummy response if model not loaded:
    predicted_class = "dummy_class"
    confidence = 0.99

    # If you have a real model, un-comment the lines above and remove the dummy lines.

    return {
        "prediction": predicted_class,
        "confidence": round(confidence, 4)
    }
