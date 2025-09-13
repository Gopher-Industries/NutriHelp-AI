from torchvision import transforms
import torch, random
from PIL import Image
import io

class RandomJPEGCompression(torch.nn.Module):
    def __init__(self, quality_min=35, quality_max=85, p=0.7):
        super().__init__()
        self.qmin, self.qmax, self.p = quality_min, quality_max, p
    def forward(self, img: Image.Image):
        if random.random() > self.p: return img
        q = random.randint(self.qmin, self.qmax)
        buf = io.BytesIO(); img.save(buf, format="JPEG", quality=q); buf.seek(0)
        return Image.open(buf).convert("RGB")

class MixupCutmix:
    def __init__(self, mixup_alpha=0.2, cutmix_alpha=0.2, p=0.5):
        self.mixup_alpha, self.cutmix_alpha, self.p = mixup_alpha, cutmix_alpha, p
    def _rand_bbox(self, W, H, lam):
        cut_rat = (1 - lam) ** 0.5; cw, ch = int(W*cut_rat), int(H*cut_rat)
        cx, cy = random.randint(0, W), random.randint(0, H)
        x1, y1 = max(cx - cw//2, 0), max(cy - ch//2, 0)
        x2, y2 = min(cx + cw//2, W), min(cy + ch//2, H)
        return x1, y1, x2, y2
    def __call__(self, x, y):
        import torch
        if random.random() > self.p or len(x) < 2: return x, y
        use_cutmix = random.random() < 0.5 and self.cutmix_alpha > 0
        alpha = self.cutmix_alpha if use_cutmix else self.mixup_alpha
        lam = torch.distributions.Beta(alpha, alpha).sample().item()
        idx = torch.randperm(x.size(0), device=x.device)
        x2, y2 = x[idx], y[idx]
        if use_cutmix:
            B, C, H, W = x.shape
            x1, y1, x2c, y2c = self._rand_bbox(W, H, lam)
            x[:, :, y1:y2c, x1:x2c] = x2[:, :, y1:y2c, x1:x2c]
            lam = 1 - ((x2c - x1) * (y2c - y1) / (W * H))
            y = lam * y + (1 - lam) * y2
            return x, y
        else:
            return lam * x + (1 - lam) * x2, lam * y + (1 - lam) * y2

def build_transforms(image_size=320):
    train_tfms = transforms.Compose([
        transforms.RandomResizedCrop(image_size, scale=(0.6, 1.0)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomApply([transforms.ColorJitter(0.3,0.3,0.3,0.15)], p=0.7),
        transforms.RandomApply([transforms.GaussianBlur(kernel_size=3)], p=0.3),
        transforms.RandomApply([transforms.RandomPerspective(distortion_scale=0.4)], p=0.2),
        RandomJPEGCompression(35, 85, p=0.7),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.485,0.456,0.406), std=(0.229,0.224,0.225)),
        transforms.RandomErasing(p=0.25, scale=(0.02,0.1), ratio=(0.3,3.3)),
    ])
    val_tfms = transforms.Compose([
        transforms.Resize(int(image_size*1.15)),
        transforms.CenterCrop(image_size),
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.485,0.456,0.406), std=(0.229,0.224,0.225)),
    ])
    return train_tfms, val_tfms
