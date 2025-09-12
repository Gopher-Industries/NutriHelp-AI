import torch, json
import pandas as pd, numpy as np
import torch.nn as nn

def compute_pos_weight_from_csv(train_csv, num_classes):
    df = pd.read_csv(train_csv)
    pos = np.zeros(num_classes, dtype=np.float64)
    for s in df["labels"]:
        for k in json.loads(s):
            if 0 <= k < num_classes: pos[k] += 1
    N = len(df); neg = N - pos
    pos_weight = torch.tensor((neg / np.maximum(pos, 1e-8)).tolist(), dtype=torch.float32)
    return torch.clamp(pos_weight, max=100.0)

class AsymmetricLoss(nn.Module):
    def __init__(self, gp=0, gn=4, clip=0.05, eps=1e-8):
        super().__init__(); self.gp, self.gn, self.clip, self.eps = gp, gn, clip, eps
    def forward(self, logits, targets):
        x = torch.sigmoid(logits); xp, xn = x, 1 - x
        if self.clip and self.clip > 0: xn = (xn + self.clip).clamp(max=1)
        lp = targets * torch.log(xp.clamp(min=self.eps))
        ln = (1 - targets) * torch.log(xn.clamp(min=self.eps))
        if self.gp > 0 or self.gn > 0:
            ptp, ptn = xp * targets, xn * (1 - targets)
            lp *= (1 - ptp) ** self.gp; ln *= (ptn) ** self.gn
        return - (lp + ln).mean()
