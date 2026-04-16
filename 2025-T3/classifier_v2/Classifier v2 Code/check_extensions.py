import os

DATASET_PATH = "dataset_v2"  # change if your dataset name is different

def list_extensions(split_name):
    folder = os.path.join(DATASET_PATH, split_name)
    extensions = set()

    print(f"\nChecking {split_name.upper()} split...")

    for class_name in sorted(os.listdir(folder)):
        class_folder = os.path.join(folder, class_name)
        if os.path.isdir(class_folder):
            for f in os.listdir(class_folder):
                ext = os.path.splitext(f)[1].lower().strip()
                if ext:
                    extensions.add(ext)

    print(f"Extensions found in {split_name}: {extensions}")

list_extensions("train")
list_extensions("val")
list_extensions("test")
