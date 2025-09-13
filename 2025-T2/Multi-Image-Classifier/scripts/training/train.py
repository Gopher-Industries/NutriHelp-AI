import sys, os, math, json, time, argparse, contextlib
from pathlib import Path
_here = Path(__file__).resolve().parent     
_scripts = _here.parent                     
if str(_scripts) not in sys.path: sys.path.append(str(_scripts))

import torch, torch.nn as nn
from torch import amp
from training.model import MultiLabelBackbone
from training.augment import MixupCutmix
from training.metrics import multilabel_f1_from_logits, multilabel_accuracy_from_logits
from training.losses import compute_pos_weight_from_csv, AsymmetricLoss
from training.ema import ModelEMA
from dataloader import get_vfn_dataloaders

@contextlib.contextmanager
def chdir(path: Path):
    old = Path.cwd(); os.chdir(path)
    try: yield
    finally: os.chdir(old)

def cosine_scheduler(optimizer, warmup_epochs, total_epochs, base_lr, min_lr=1e-6, steps_per_epoch=1):
    def lr_lambda(it):
        ep = it / steps_per_epoch
        if ep < warmup_epochs: return (ep + 1) / max(warmup_epochs, 1)
        prog = (ep - warmup_epochs) / max((total_epochs - warmup_epochs), 1e-9)
        return min_lr / base_lr + 0.5 * (1 - min_lr / base_lr) * (1 + math.cos(math.pi * prog))
    return torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)

def _evaluate(model, loader, device, threshold=0.5):
    model.eval(); logits_all, targets_all = [], []
    with torch.no_grad(), amp.autocast('cuda', enabled=False):
        for imgs, targets in loader:
            imgs, targets = imgs.to(device), targets.to(device)
            logits_all.append(model(imgs).cpu()); targets_all.append(targets.cpu())
    logits_all, targets_all = torch.cat(logits_all, 0), torch.cat(targets_all, 0)
    f1 = multilabel_f1_from_logits(logits_all, targets_all, threshold=threshold, average="micro")
    acc = multilabel_accuracy_from_logits(logits_all, targets_all, threshold=threshold)
    return f1, acc

def train(args):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    scripts_dir = _scripts
    processed_dir = (scripts_dir / "processed").resolve() if args.processed_dir == "scripts/processed" else Path(args.processed_dir).resolve()
    vfn_root = (scripts_dir / "VFN") if args.vfn_root == "scripts/VFN" else Path(args.vfn_root)

    repo_root = scripts_dir.parent.parent.parent
    weights_dir = Path(args.weights_dir).resolve() if args.weights_dir else (repo_root / "models")
    weights_dir.mkdir(parents=True, exist_ok=True)
    final_path = weights_dir / "multi_image_classifier.pt"

    classes = json.load(open(processed_dir / "classes.json")); num_classes = len(classes)
    model = MultiLabelBackbone(args.model_name, num_classes, pretrained=True).to(device)

    criterion = (AsymmetricLoss(gp=0, gn=4, clip=0.05) if args.loss == "asl"
                 else nn.BCEWithLogitsLoss(pos_weight=compute_pos_weight_from_csv(str(processed_dir/"train.csv"), num_classes).to(device)))

    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=0.05)
    scaler = amp.GradScaler('cuda', enabled=True)
    mixcut = MixupCutmix(args.mixup_alpha, args.cutmix_alpha, p=0.5) if args.use_mixcut else None
    ema = ModelEMA(model, decay=0.9998, device=device) if args.use_ema else None

  
    with chdir(vfn_root.resolve()):
        train_loader, val_loader, test_loader = get_vfn_dataloaders(
            data_dir=str(processed_dir), batch_size=args.batch_size, image_size=(args.image_size, args.image_size)
        )

        steps = max(1, len(train_loader))
        sched = cosine_scheduler(optimizer, args.warmup_epochs, args.epochs, args.lr, args.min_lr, steps)
        best_val = -1.0; t0 = time.time()

        for epoch in range(1, args.epochs + 1):
            model.train(); total_loss = 0.0
            for imgs, targets in train_loader:
                imgs, targets = imgs.to(device, non_blocking=True), targets.to(device, non_blocking=True)
                if mixcut is not None: imgs, targets = mixcut(imgs, targets)
                optimizer.zero_grad(set_to_none=True)
                with amp.autocast('cuda', enabled=True):
                    loss = criterion(model(imgs), targets)
                scaler.scale(loss).backward()
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                scaler.step(optimizer); scaler.update(); sched.step()
                if ema is not None: ema.update(model)
                total_loss += loss.item()

            eval_model = ema.ema if ema is not None else model
            val_f1, val_acc = _evaluate(eval_model, val_loader, device, args.eval_threshold)
            print(f"Epoch {epoch:03d}/{args.epochs} | loss {total_loss/steps:.4f} | Val_F1 {val_f1:.4f} | Val_Acc {val_acc:.4f}")

            
            if val_f1 > best_val:
                best_val = val_f1
                torch.save({"model": eval_model.state_dict(),
                            "num_classes": num_classes,
                            "model_name": args.model_name}, final_path)

        mins = (time.time() - t0)/60
        print(f"Done in {mins:.1f} min. Best Val F1_micro: {best_val:.4f}")
        train_f1, train_acc = _evaluate(eval_model, train_loader, device, args.eval_threshold)
        test_f1, test_acc = _evaluate(eval_model, test_loader, device, args.eval_threshold)
        print(f"\nFinal Train: F1_micro={train_f1:.4f}, Acc={train_acc:.4f}")
        print(f"Final Test : F1_micro={test_f1:.4f}, Acc={test_acc:.4f}")
        print(f"Saved FINAL model to: {final_path}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--processed_dir", type=str, default="scripts/processed")
    ap.add_argument("--vfn_root", type=str, default="scripts/VFN")
    ap.add_argument("--weights_dir", type=str, default="") 
    ap.add_argument("--model_name", type=str, default="convnext_tiny")
    ap.add_argument("--batch_size", type=int, default=64)
    ap.add_argument("--image_size", type=int, default=320)
    ap.add_argument("--epochs", type=int, default=80)
    ap.add_argument("--warmup_epochs", type=int, default=5)
    ap.add_argument("--lr", type=float, default=5e-4)
    ap.add_argument("--min_lr", type=float, default=1e-6)
    ap.add_argument("--use_ema", action="store_true", default=True)
    ap.add_argument("--use_mixcut", action="store_true", default=True)
    ap.add_argument("--mixup_alpha", type=float, default=0.2)
    ap.add_argument("--cutmix_alpha", type=float, default=0.2)
    ap.add_argument("--loss", type=str, choices=["bce","asl"], default="bce")
    ap.add_argument("--eval_threshold", type=float, default=0.5)
    args = ap.parse_args(); train(args)
