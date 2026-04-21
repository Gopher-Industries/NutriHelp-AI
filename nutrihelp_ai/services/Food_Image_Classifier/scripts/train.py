import argparse
from pathlib import Path

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import accuracy_score, classification_report
from tqdm import tqdm

try:
    from .model import FoodClassifier
    from .prepare_data import get_food101_dataloaders
except ImportError:  # pragma: no cover - script execution fallback
    from model import FoodClassifier
    from prepare_data import get_food101_dataloaders


DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
DEFAULT_MODEL_PATH = Path(__file__).resolve().parent.parent / "outputs" / "models" / "food_classifier.pth"


def train(args):
    train_loader, test_loader, class_names = get_food101_dataloaders(
        data_dir=args.data_dir,
        batch_size=args.batch_size,
        image_size=args.image_size,
        num_workers=args.num_workers,
        normalization="imagenet",
    )

    model = FoodClassifier(num_classes=len(class_names)).to(DEVICE)
    criterion = nn.CrossEntropyLoss(label_smoothing=args.label_smoothing)
    optimizer = optim.AdamW(
        model.parameters(),
        lr=args.learning_rate,
        weight_decay=args.weight_decay,
    )
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=max(args.epochs, 1))

    for epoch in range(args.epochs):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0

        loop = tqdm(train_loader, desc=f"Epoch {epoch + 1}/{args.epochs}")
        for images, labels in loop:
            images = images.to(DEVICE, non_blocking=True)
            labels = labels.to(DEVICE, non_blocking=True)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            running_loss += loss.item()
            loop.set_postfix(loss=loss.item(), acc=100 * correct / max(total, 1))

        scheduler.step()
        print(
            f"Epoch [{epoch + 1}/{args.epochs}] "
            f"Loss: {running_loss:.4f} "
            f"Accuracy: {100 * correct / max(total, 1):.2f}%"
        )

    print("\nEvaluation")
    model.eval()
    y_true = []
    y_pred = []
    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(DEVICE, non_blocking=True)
            labels = labels.to(DEVICE, non_blocking=True)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            y_true.extend(labels.cpu().numpy())
            y_pred.extend(predicted.cpu().numpy())

    test_acc = accuracy_score(y_true, y_pred)
    print(f"Final Test Accuracy: {100 * test_acc:.2f}%")
    print(classification_report(y_true, y_pred))

    model_path = Path(args.model_save_path).resolve()
    model_path.parent.mkdir(parents=True, exist_ok=True)
    checkpoint = {
        "model_state": model.state_dict(),
        "classes": class_names,
        "image_size": args.image_size,
        "normalization": "imagenet",
        "backbone": "efficientnet_b0",
    }
    torch.save(checkpoint, model_path)
    print(f"Model saved to {model_path}")


def build_parser():
    parser = argparse.ArgumentParser(description="Train the single-image food classifier.")
    parser.add_argument("--data-dir", type=str, default="data")
    parser.add_argument("--epochs", type=int, default=15)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--image-size", type=int, default=320)
    parser.add_argument("--learning-rate", type=float, default=3e-4)
    parser.add_argument("--weight-decay", type=float, default=1e-4)
    parser.add_argument("--label-smoothing", type=float, default=0.1)
    parser.add_argument("--num-workers", type=int, default=2)
    parser.add_argument("--model-save-path", type=str, default=str(DEFAULT_MODEL_PATH))
    return parser


if __name__ == "__main__":
    train(build_parser().parse_args())
