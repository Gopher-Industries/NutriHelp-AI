import torch
from torchvision import transforms


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



# import torch
# from torchvision import transforms
# import timm
# from PIL import Image

# MODEL_NAME = 'resnet50d'
# MODEL_WEIGHTS_PATH = "models/resnet50d_14epochs_accuracy0.99144_weights.pth"
# NUM_CLASSES = 101  # update with your actual number of classes
# DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# # Load the model exactly as trained
# model = timm.create_model(MODEL_NAME, pretrained=False)
# n_features = model.fc.in_features
# model.fc = torch.nn.Linear(n_features, NUM_CLASSES)

# # Load weights
# state_dict = torch.load(MODEL_WEIGHTS_PATH, map_location=DEVICE)
# model.load_state_dict(state_dict)

# model.to(DEVICE)
# model.eval()

# # Define transforms
# def transform_image(image):
#     transform = transforms.Compose([
#         transforms.Resize((224, 224)),
#         transforms.ToTensor(),
#         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
#     ])
#     return transform(image).unsqueeze(0).to(DEVICE)

# # Prediction function
# def predict_image_service(image):
#     tensor = transform_image(image)
#     with torch.no_grad():
#         outputs = model(tensor)
#         probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
#         confidence, predicted_class = torch.max(probabilities, 0)

#     class_names = ["class1", "class2", "class3"]  # update with your actual class names
#     predicted_label = class_names[predicted_class.item()]

#     return {
#         "prediction": predicted_label,
#         "confidence": confidence.item()
#     }