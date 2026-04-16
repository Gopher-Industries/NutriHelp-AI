"""
classifying_v2_training.py

Train and evaluate NutriHelp food classifier v2 using transfer learning (MobileNetV2) on dataset_v2_augmented.

Folder structure (relative to this script):
    dataset_v2_augmented/
        train/
        val/
        test/
"""

import os
import time
import copy
import random

import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models

# -----------------------------
# Configuration
# -----------------------------
DATA_ROOT = "dataset_v2_augmented"   # folder created in Week 5
IMG_SIZE = 224
BATCH_SIZE = 16
NUM_EPOCHS = 5          # you can increase later if training is stable
LEARNING_RATE = 1e-4
WEIGHT_DECAY = 1e-4
NUM_WORKERS = 2         # set to 0 if you get DataLoader issues

OUTPUT_DIR = "models"
os.makedirs(OUTPUT_DIR, exist_ok=True)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {DEVICE}")

# -----------------------------
# Reproducibility
# -----------------------------
SEED = 42
random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False

# -----------------------------
# Data transforms & loaders
# -----------------------------
train_dir = os.path.join(DATA_ROOT, "train")
val_dir = os.path.join(DATA_ROOT, "val")
test_dir = os.path.join(DATA_ROOT, "test")

train_transforms = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    # Normalisation values are standard ImageNet stats
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

eval_transforms = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

train_dataset = datasets.ImageFolder(train_dir, transform=train_transforms)
val_dataset = datasets.ImageFolder(val_dir, transform=eval_transforms)
test_dataset = datasets.ImageFolder(test_dir, transform=eval_transforms)

class_names = train_dataset.classes
num_classes = len(class_names)

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=0)
val_loader   = DataLoader(val_dataset,   batch_size=BATCH_SIZE, shuffle=False, num_workers=0)
test_loader  = DataLoader(test_dataset,  batch_size=BATCH_SIZE, shuffle=False, num_workers=0)

print("Train dir:", os.path.abspath(train_dir))
print("Val dir:  ", os.path.abspath(val_dir))
print("Test dir: ", os.path.abspath(test_dir))
print(f"Train size: {len(train_dataset)}")
print(f"Val size:   {len(val_dataset)}")
print(f"Test size:  {len(test_dataset)}")
print(f"Classes:    {class_names}")

# -----------------------------
# Model: MobileNetV2 (transfer learning)
# -----------------------------
def create_model(num_classes: int) -> nn.Module:
    """
    Load a pretrained MobileNetV2 and replace the final layer
    to match our number of classes.
    """
    try:
        # Newer torchvision style
        weights = models.MobileNet_V2_Weights.DEFAULT
        model = models.mobilenet_v2(weights=weights)
    except AttributeError:
        # Fallback for older torchvision
        model = models.mobilenet_v2(pretrained=True)

    # Freeze backbone if you want faster training (optional)
    for param in model.features.parameters():
        param.requires_grad = True  # set False to freeze

    # Replace classifier head
    in_features = model.classifier[1].in_features
    model.classifier[1] = nn.Linear(in_features, num_classes)

    return model


model = create_model(num_classes).to(DEVICE)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE,
                       weight_decay=WEIGHT_DECAY)
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=2, gamma=0.1)

# -----------------------------
# Training / evaluation helpers
# -----------------------------
def run_one_epoch(model, dataloader, optimizer=None):
    """
    If optimizer is provided -> training mode.
    If optimizer is None      -> evaluation mode.
    Returns: (epoch_loss, epoch_acc)
    """
    if optimizer is None:
        model.eval()
        phase = "val/test"
    else:
        model.train()
        phase = "train"

    running_loss = 0.0
    running_corrects = 0

    dataset_size = len(dataloader.dataset)

    for inputs, labels in dataloader:
        inputs = inputs.to(DEVICE)
        labels = labels.to(DEVICE)

        if optimizer is not None:
            optimizer.zero_grad()

        with torch.set_grad_enabled(optimizer is not None):
            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)
            loss = criterion(outputs, labels)

            if optimizer is not None:
                loss.backward()
                optimizer.step()

        running_loss += loss.item() * inputs.size(0)
        running_corrects += torch.sum(preds == labels.data)

    epoch_loss = running_loss / dataset_size
    epoch_acc = running_corrects.double() / dataset_size

    return epoch_loss, epoch_acc.item()


def evaluate_on_test(model, dataloader, class_names):
    """
    Compute overall accuracy and per-class accuracy on the test set.
    """
    model.eval()
    total_correct = 0
    total_samples = 0

    per_class_correct = {c: 0 for c in class_names}
    per_class_total = {c: 0 for c in class_names}

    with torch.no_grad():
        for inputs, labels in dataloader:
            inputs = inputs.to(DEVICE)
            labels = labels.to(DEVICE)

            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)

            total_correct += torch.sum(preds == labels).item()
            total_samples += labels.size(0)

            for label, pred in zip(labels, preds):
                class_name = class_names[label.item()]
                per_class_total[class_name] += 1
                if label == pred:
                    per_class_correct[class_name] += 1

    overall_acc = total_correct / total_samples

    per_class_acc = {}
    for cls in class_names:
        if per_class_total[cls] > 0:
            per_class_acc[cls] = per_class_correct[cls] / per_class_total[cls]
        else:
            per_class_acc[cls] = 0.0

    return overall_acc, per_class_acc


# -----------------------------
# Main training loop
# -----------------------------
best_model_wts = copy.deepcopy(model.state_dict())
best_val_acc = 0.0

print("\nStarting training...\n")
start_time = time.time()

for epoch in range(NUM_EPOCHS):
    print(f"Epoch {epoch + 1}/{NUM_EPOCHS}")
    print("-" * 30)

    train_loss, train_acc = run_one_epoch(model, train_loader, optimizer)
    val_loss, val_acc = run_one_epoch(model, val_loader, optimizer=None)

    scheduler.step()

    print(f"Train Loss: {train_loss:.4f}  |  Train Acc: {train_acc:.4f}")
    print(f"Val   Loss: {val_loss:.4f}  |  Val   Acc: {val_acc:.4f}")

    # Save best model (based on validation accuracy)
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        best_model_wts = copy.deepcopy(model.state_dict())
        save_path = os.path.join(OUTPUT_DIR, "classifier_v2_mobilenet_best.pth")
        torch.save(best_model_wts, save_path)
        print(f"New best model saved to {save_path}")

    print()

elapsed = time.time() - start_time
print(f"Training complete in {elapsed/60:.1f} minutes")
print(f"Best val accuracy: {best_val_acc:.4f}")

# -----------------------------
# Load best model & evaluate on test set
# -----------------------------
print("\nEvaluating best model on TEST set...\n")
model.load_state_dict(best_model_wts)

test_acc, per_class_acc = evaluate_on_test(model, test_loader, class_names)

print(f"Overall TEST accuracy: {test_acc:.4f}")
print("\nPer-class TEST accuracy:")
for cls in class_names:
    print(f"  {cls:12s}: {per_class_acc[cls]:.4f}")

# Save a small text summary for your report
summary_path = os.path.join(OUTPUT_DIR, "classifier_v2_results.txt")
with open(summary_path, "w", encoding="utf-8") as f:
    f.write(f"Best validation accuracy: {best_val_acc:.4f}\n")
    f.write(f"Overall test accuracy:   {test_acc:.4f}\n\n")
    f.write("Per-class test accuracy:\n")
    for cls in class_names:
        f.write(f"{cls:12s}: {per_class_acc[cls]:.4f}\n")

print(f"\nResults summary saved to {summary_path}")
print("Done")