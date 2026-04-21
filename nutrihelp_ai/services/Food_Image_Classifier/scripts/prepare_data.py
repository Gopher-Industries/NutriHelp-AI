from pathlib import Path

from torch.utils.data import DataLoader
from torchvision.datasets import Food101

try:
    from .augment import build_eval_transform, build_train_transform
except ImportError:  # pragma: no cover - script execution fallback
    from augment import build_eval_transform, build_train_transform


def get_food101_dataloaders(
    data_dir="data",
    batch_size: int = 32,
    image_size: int = 320,
    num_workers: int = 2,
    normalization: str = "imagenet",
):
    root = Path(data_dir).resolve()
    train_transform = build_train_transform(image_size=image_size, normalization=normalization)
    eval_transform = build_eval_transform(image_size=image_size, normalization=normalization)

    train_dataset = Food101(root=str(root), split="train", download=True, transform=train_transform)
    test_dataset = Food101(root=str(root), split="test", download=True, transform=eval_transform)

    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
        pin_memory=True,
    )
    test_loader = DataLoader(
        test_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=True,
    )

    return train_loader, test_loader, list(train_dataset.classes)
