import torch

@torch.no_grad()
def multilabel_f1_from_logits(logits, targets, threshold=0.5, average="micro"):
    probs = torch.sigmoid(logits); preds = (probs >= threshold).float()
    tp = (preds * targets).sum(dim=0)
    fp = ((preds == 1) & (targets == 0)).sum(dim=0)
    fn = ((preds == 0) & (targets == 1)).sum(dim=0)
    f1 = (2*tp) / (2*tp + fp + fn + 1e-8)
    if average == "macro": return f1.mean().item()
    return (2*tp.sum() / (2*tp.sum() + fp.sum() + fn.sum() + 1e-8)).item()

@torch.no_grad()
def multilabel_accuracy_from_logits(logits, targets, threshold=0.5):
    probs = torch.sigmoid(logits); preds = (probs >= threshold).float()
    return (preds == targets).float().mean().item()
