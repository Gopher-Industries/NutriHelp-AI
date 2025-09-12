import sys
from pathlib import Path
_here = Path(__file__).resolve().parent          
_scripts = _here.parent                        
if str(_scripts) not in sys.path:
    sys.path.append(str(_scripts))

import os, json, argparse, glob, io
from typing import List, Optional, Dict, Any
import torch
from PIL import Image
from training.model import MultiLabelBackbone
from training.augment import build_transforms

def _resolve_under_scripts(arg_path: str) -> Path:
    p = Path(arg_path)
    if p.is_absolute():
        return p
    parts = p.parts
    if len(parts) >= 2 and parts[0] == "scripts" and parts[1] == "processed":
        return (_scripts / "processed").resolve()
    if len(parts) == 1 and parts[0] == "processed":
        return (_scripts / "processed").resolve()
    return (_scripts / p).resolve()

class Predictor:
    def __init__(
        self,
        processed_dir: str = "scripts/processed",
        weights_dir: Optional[str] = None,
        model_name_fallback: str = "convnext_tiny",
        image_size: int = 320,
        default_threshold: float = 0.5,
        device: Optional[str] = None
    ):
        self.device = torch.device(device) if device else torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.processed_dir = _resolve_under_scripts(processed_dir)

        repo_root = Path(__file__).resolve().parents[4]
        self.weights_dir = Path(weights_dir).resolve() if weights_dir else (repo_root / "models")
        self.model_file = self.weights_dir / "multi_image_classifier.pt"

        with open(self.processed_dir / "classes.json", "r") as f:
            self.classes: List[str] = json.load(f)
        self.num_classes = len(self.classes)

        thr_path = self.processed_dir / "best_thresholds.json"
        if thr_path.exists():
            th = json.load(open(thr_path, "r"))
            self.thresholds = torch.tensor(th, dtype=torch.float32)
            if len(self.thresholds) != self.num_classes:
                self.thresholds = torch.full((self.num_classes,), default_threshold)
        else:
            self.thresholds = torch.full((self.num_classes,), default_threshold)

        ckpt = torch.load(str(self.model_file), map_location="cpu")
        model_name = ckpt.get("model_name", model_name_fallback)
        self.model = MultiLabelBackbone(model_name, self.num_classes, pretrained=False)
        state = ckpt.get("model", ckpt)
        self.model.load_state_dict(state)
        self.model.to(self.device).eval()

        _, val_tfms = build_transforms(image_size=image_size)
        self.transform = val_tfms

    def _pil_from_bytes(self, b: bytes) -> Image.Image:
        return Image.open(io.BytesIO(b)).convert("RGB")

    @torch.no_grad()
    def predict_from_bytes(self, image_bytes: bytes, topk: Optional[int] = None) -> Dict[str, Any]:
        img = self._pil_from_bytes(image_bytes)
        x = self.transform(img).unsqueeze(0) 
        probs = torch.sigmoid(self.model(x.to(self.device))).cpu().squeeze(0)

        mask = probs >= self.thresholds
        idx = torch.nonzero(mask).flatten().tolist()
        labels = [self.classes[j] for j in idx]
        confs = [float(probs[j]) for j in idx]
        out = {"labels": labels, "confidences": confs, "scores": probs.tolist()}
        if topk:
            tk = min(topk, self.num_classes)
            top_idx = torch.topk(probs, k=tk).indices.tolist()
            out["topk_labels"] = [self.classes[j] for j in top_idx]
            out["topk_scores"] = [float(probs[j]) for j in top_idx]
        else:
            out["topk_labels"], out["topk_scores"] = [], []
        return out

    @torch.no_grad()
    def predict_paths(self, image_paths: List[str], topk: Optional[int] = None) -> List[Dict[str, Any]]:
        out, batch, valid = [], [], []
        for p in image_paths:
            if not os.path.isfile(p):
                print(f"[WARN] file not found: {p}")
                continue
            batch.append(self.transform(Image.open(p).convert("RGB")))
            valid.append(p)
        if not batch:
            return out
        X = torch.stack(batch, 0).to(self.device)
        probs = torch.sigmoid(self.model(X)).cpu()
        for i, p in enumerate(valid):
            pr = probs[i]
            mask = pr >= self.thresholds
            idx = torch.nonzero(mask).flatten().tolist()
            labels = [self.classes[j] for j in idx]
            confs = [float(pr[j]) for j in idx]
            item = {"image_path": p, "labels": labels, "confidences": confs, "scores": pr.tolist()}
            if topk:
                tk = min(topk, self.num_classes)
                top_idx = torch.topk(pr, k=tk).indices.tolist()
                item["topk_labels"] = [self.classes[j] for j in top_idx]
                item["topk_scores"] = [float(pr[j]) for j in top_idx]
            else:
                item["topk_labels"], item["topk_scores"] = [], []
            out.append(item)
        return out


def _expand_patterns(paths: List[str]) -> List[str]:
    out = []
    for item in paths:
        if any(ch in item for ch in ["*", "?", "["]):
            out.extend(glob.glob(item))
        else:
            out.append(item)
    return out

def main():
    ap = argparse.ArgumentParser(description="Predict with final multi-image classifier.")
    ap.add_argument("--processed_dir", type=str, default="scripts/processed")
    ap.add_argument("--weights_dir", type=str, default="", help="blank -> auto-use <repo_root>/models")
    ap.add_argument("--images", nargs="+", default=None, help="paths or globs")
    ap.add_argument("--topk", type=int, default=5)
    ap.add_argument("--image_size", type=int, default=320)
    ap.add_argument("--out_json", type=str, default="")
    args = ap.parse_args()

    weights_dir = None if args.weights_dir == "" else args.weights_dir
    predictor = Predictor(processed_dir=args.processed_dir, weights_dir=weights_dir, image_size=args.image_size)

    if not args.images:
        raise SystemExit("No images provided. Use --images (for API, call Predictor.predict_from_bytes).")

    paths = _expand_patterns(args.images)
    res = predictor.predict_paths(paths, topk=args.topk)

    for r in res:
        print(f"\n{r.get('image_path', '<bytes>')}")
        print("  labels:", r["labels"])
        if r["labels"]:
            print("  confs :", [round(c, 3) for c in r["confidences"]])

    if args.out_json:
        Path(args.out_json).parent.mkdir(parents=True, exist_ok=True)
        json.dump(res, open(args.out_json, "w"))
        print(f"\nSaved to {args.out_json}")

if __name__ == "__main__":
    main()
