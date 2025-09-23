import os
import json
import pandas as pd
from collections import defaultdict

def preprocess_vfn_dataset(data_dir="VFN", output_dir="processed"):
    meta_dir = os.path.join(data_dir, "Meta")
    image_dir = os.path.join(data_dir, "Images")

    classes = []
    with open(os.path.join(meta_dir, "category_ids.txt")) as f:
        for line in f:
            idx, name = line.strip().split(maxsplit=1)
            classes.append(name)

    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "classes.json"), "w") as f:
        json.dump(classes, f)

    annotations_file = os.path.join(meta_dir, "annotations.txt")
    img_to_labels = defaultdict(list)

    with open(annotations_file) as f:
        for line in f:
            parts = line.strip().split()
            img_name = parts[0]
            class_id = int(parts[-1])  
            img_to_labels[img_name].append(class_id)

    imgname_to_path = {}
    for root, _, files in os.walk(image_dir):
        for fname in files:
            if fname.lower().endswith(".jpg"):
                rel_path = os.path.relpath(os.path.join(root, fname), data_dir)
                imgname_to_path[fname] = rel_path

    def parse_split(split_file, split_name):
        rows = []
        with open(os.path.join(meta_dir, split_file)) as f:
            for line in f:
                img_name = line.strip()
                rel_path = imgname_to_path.get(img_name)
                labels = img_to_labels.get(img_name)

                if rel_path is None or not labels:
                    continue

                rows.append({
                    "image": rel_path,
                    "labels": json.dumps(list(set(labels))) 
                })

        df = pd.DataFrame(rows)
        df.to_csv(os.path.join(output_dir, f"{split_name}.csv"), index=False)

    parse_split("training.txt", "train")
    parse_split("validation.txt", "val")
    parse_split("testing.txt", "test")

    print(f"Preprocessing done! CSV + JSON saved in {output_dir}/")

if __name__ == "__main__":
    preprocess_vfn_dataset()
