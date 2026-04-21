import io
import random
from typing import Sequence, Tuple

import torch
from PIL import Image
from torchvision import transforms


IMAGENET_MEAN = (0.485, 0.456, 0.406)
IMAGENET_STD = (0.229, 0.224, 0.225)
LEGACY_MEAN = (0.5, 0.5, 0.5)
LEGACY_STD = (0.5, 0.5, 0.5)


class RandomJPEGCompression(torch.nn.Module):
    def __init__(self, quality_min: int = 40, quality_max: int = 90, p: float = 0.5):
        super().__init__()
        self.quality_min = quality_min
        self.quality_max = quality_max
        self.p = p

    def forward(self, img: Image.Image) -> Image.Image:
        if random.random() > self.p:
            return img

        quality = random.randint(self.quality_min, self.quality_max)
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG", quality=quality)
        buffer.seek(0)
        return Image.open(buffer).convert("RGB")


def _resolve_image_size(image_size) -> int:
    if isinstance(image_size, int):
        return image_size
    if isinstance(image_size, Sequence) and image_size:
        return int(image_size[0])
    return 224


def _resolve_norm(normalization: str) -> Tuple[Tuple[float, ...], Tuple[float, ...]]:
    if normalization == "imagenet":
        return IMAGENET_MEAN, IMAGENET_STD
    return LEGACY_MEAN, LEGACY_STD


def build_train_transform(image_size=320, normalization: str = "imagenet"):
    size = _resolve_image_size(image_size)
    mean, std = _resolve_norm(normalization)
    return transforms.Compose(
        [
            transforms.RandomResizedCrop(size, scale=(0.55, 1.0)),
            transforms.RandomHorizontalFlip(),
            transforms.RandomApply([transforms.ColorJitter(0.25, 0.25, 0.25, 0.1)], p=0.7),
            transforms.RandomApply([transforms.GaussianBlur(kernel_size=3)], p=0.25),
            transforms.RandomApply([transforms.RandomPerspective(distortion_scale=0.2)], p=0.15),
            RandomJPEGCompression(40, 90, p=0.5),
            transforms.ToTensor(),
            transforms.Normalize(mean=mean, std=std),
            transforms.RandomErasing(p=0.2, scale=(0.02, 0.08), ratio=(0.3, 3.3)),
        ]
    )


def build_eval_transform(image_size=320, normalization: str = "imagenet"):
    size = _resolve_image_size(image_size)
    mean, std = _resolve_norm(normalization)
    return transforms.Compose(
        [
            transforms.Resize(int(size * 1.15)),
            transforms.CenterCrop(size),
            transforms.ToTensor(),
            transforms.Normalize(mean=mean, std=std),
        ]
    )
