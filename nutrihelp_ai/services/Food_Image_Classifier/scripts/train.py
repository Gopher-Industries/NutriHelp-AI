import sys
sys.path.append('/content/NutriHelp-AI/2025-T1/Food-Image-Classifier/scripts')

import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm
import os
from sklearn.metrics import accuracy_score, classification_report

from prepare_data import get_food101_dataloaders
from model import FoodClassifier

NUM_CLASSES = 101
NUM_EPOCHS = 15
BATCH_SIZE = 32
IMAGE_SIZE = (224, 224)
LEARNING_RATE = 0.001
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
MODEL_SAVE_PATH = '../outputs/models/food_classifier.pth'

train_loader, test_loader = get_food101_dataloaders(batch_size=BATCH_SIZE, image_size=IMAGE_SIZE)

model = FoodClassifier(num_classes=NUM_CLASSES).to(DEVICE)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

for epoch in range(NUM_EPOCHS):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    loop = tqdm(train_loader, desc=f"Epoch {epoch+1}/{NUM_EPOCHS}")
    for images, labels in loop:
        images, labels = images.to(DEVICE), labels.to(DEVICE)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

        running_loss += loss.item()
        loop.set_postfix(loss=loss.item(), acc=100 * correct / total)

    print(f"Epoch [{epoch+1}/{NUM_EPOCHS}], Loss: {running_loss:.4f}, Accuracy: {100 * correct / total:.2f}%")



print("\nEvaluation")
model.eval()
y_true = []
y_pred = []

with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(DEVICE), labels.to(DEVICE)
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        y_true.extend(labels.cpu().numpy())
        y_pred.extend(predicted.cpu().numpy())

test_acc = accuracy_score(y_true, y_pred)
print(f"Final Test Accuracy: {100 * test_acc:.2f}%")
print("\n")
print(classification_report(y_true, y_pred))


os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)
torch.save(model.state_dict(), MODEL_SAVE_PATH)
print(f"Model saved to {MODEL_SAVE_PATH}")