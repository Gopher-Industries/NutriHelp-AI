import sys
from pathlib import Path
_here = Path(__file__).resolve().parent
_scripts = _here.parent
if str(_scripts) not in sys.path: sys.path.append(str(_scripts))

import argparse, json, torch, os, contextlib
from dataloader import get_vfn_dataloaders
from training.model import MultiLabelBackbone

@torch.no_grad()
def find_best_thresholds(logits, targets, grid=None):
    if grid is None: grid = torch.linspace(0.05, 0.95, steps=19)
    C = logits.shape[1]; best = torch.zeros(C)
    probs = torch.sigmoid(logits)
    for c in range(C):
        y, pc = targets[:, c], probs[:, c]; f1s = []
        for t in grid:
            pred = (pc >= t).float()
            tp = (pred * y).sum(); fp = ((pred==1)&(y==0)).sum(); fn = ((pred==0)&(y==1)).sum()
            f1s.append((2*tp / (2*tp + fp + fn + 1e-8)).item())
        best[c] = grid[torch.tensor(f1s).argmax()]
    return best

def main(args):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    scripts_dir = _scripts
    processed_dir = (scripts_dir/"processed").resolve() if args.processed_dir=="scripts/processed" else Path(args.processed_dir).resolve()
    vfn_root = (scripts_dir/"VFN") if args.vfn_root=="scripts/VFN" else Path(args.vfn_root)
    repo_root = scripts_dir.parent.parent.parent
    weights_dir = Path(args.weights_dir).resolve() if args.weights_dir else (repo_root/"models")
    final_path = weights_dir/"multi_image_classifier.pt"

    classes = json.load(open(processed_dir/"classes.json")); num_classes = len(classes)

    @contextlib.contextmanager
    def chdir(p: Path):
        old = Path.cwd(); os.chdir(p)
        try: yield
        finally: os.chdir(old)

    with chdir(vfn_root.resolve()):
        _, val_loader, _ = get_vfn_dataloaders(data_dir=str(processed_dir),
                                               batch_size=args.batch_size,
                                               image_size=(args.image_size, args.image_size))
        ckpt = torch.load(str(final_path), map_location="cpu")
        model = MultiLabelBackbone(ckpt.get("model_name","convnext_tiny"), num_classes, pretrained=False)
        state = ckpt.get("model", ckpt); model.load_state_dict(state)
        model.to(device).eval()

        logits_all, targets_all = [], []
        with torch.no_grad():
            for imgs, targets in val_loader:
                imgs = imgs.to(device); logits_all.append(model(imgs).cpu()); targets_all.append(targets)
        logits_all, targets_all = torch.cat(logits_all,0), torch.cat(targets_all,0)
        best = find_best_thresholds(logits_all, targets_all)

    out = processed_dir/"best_thresholds.json"; json.dump(best.tolist(), open(out,"w"))
    print(f"Saved per-class thresholds to {out}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--processed_dir", type=str, default="scripts/processed")
    ap.add_argument("--vfn_root", type=str, default="scripts/VFN")
    ap.add_argument("--weights_dir", type=str, default="")
    ap.add_argument("--batch_size", type=int, default=64)
    ap.add_argument("--image_size", type=int, default=320)
    args = ap.parse_args(); main(args)
