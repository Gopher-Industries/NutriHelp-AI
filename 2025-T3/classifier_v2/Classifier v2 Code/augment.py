import os
import random
from PIL import Image, ImageOps, ImageEnhance

# ==== CONFIG ====
INPUT_PATH = "dataset_v2_processed"      # use the processed dataset
OUTPUT_PATH = "dataset_v2_augmented"     # new folder with augmented images
TARGET_SIZE = (224, 224)                 # keep same size

IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png")
AUG_PER_IMAGE = 1   # how many augmented copies per original
# =================


def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def augment_image(img: Image.Image) -> Image.Image:
    """Apply a few simple random augmentations to an image."""
    # Random horizontal flip
    if random.random() < 0.5:
        img = ImageOps.mirror(img)

    # Small random rotation between -15 and +15 degrees
    angle = random.uniform(-15, 15)
    img = img.rotate(angle, expand=False)

    # Random brightness change (0.8 to 1.2)
    enhancer = ImageEnhance.Brightness(img)
    factor = random.uniform(0.8, 1.2)
    img = enhancer.enhance(factor)

    # Ensure size and mode are consistent
    img = img.convert("RGB")
    img = img.resize(TARGET_SIZE)
    return img


def process_train_split():
    input_train_dir = os.path.join(INPUT_PATH, "train")
    output_train_dir = os.path.join(OUTPUT_PATH, "train")

    if not os.path.exists(input_train_dir):
        print(f"[ERROR] Train folder not found: {input_train_dir}")
        return

    print("=== Augmenting TRAIN split ===")

    total_original = 0
    total_augmented = 0

    for class_name in sorted(os.listdir(input_train_dir)):
        input_class_dir = os.path.join(input_train_dir, class_name)
        if not os.path.isdir(input_class_dir):
            continue

        output_class_dir = os.path.join(output_train_dir, class_name)
        ensure_dir(output_class_dir)

        print(f"\nClass: {class_name}")
        for filename in os.listdir(input_class_dir):
            ext = os.path.splitext(filename)[1].lower()
            if ext not in IMAGE_EXTENSIONS:
                print(f"  [SKIP] {filename} (unsupported ext: {ext})")
                continue

            total_original += 1
            input_path = os.path.join(input_class_dir, filename)

            try:
                with Image.open(input_path) as img:
                    img = img.convert("RGB")
                    img = img.resize(TARGET_SIZE)

                    # Save a clean copy of original into augmented folder too
                    base_name = os.path.splitext(filename)[0]
                    orig_out_path = os.path.join(
                        output_class_dir, base_name + "_orig.jpg"
                    )
                    img.save(orig_out_path, format="JPEG", quality=90)

                    # Create AUG_PER_IMAGE augmented versions
                    for i in range(AUG_PER_IMAGE):
                        aug_img = augment_image(img)
                        aug_name = f"{base_name}_aug{i+1}.jpg"
                        aug_out_path = os.path.join(output_class_dir, aug_name)
                        aug_img.save(aug_out_path, format="JPEG", quality=90)
                        total_augmented += 1

            except Exception as e:
                print(f"  [SKIP] Failed to process {input_path}: {e}")

    print("\n=== Summary for augmentation ===")
    print(f"Original images processed : {total_original}")
    print(f"Augmented images created  : {total_augmented}")
    print("Output train folder       :", output_train_dir)


def copy_val_test():
    """Copy val and test splits without augmentation, to keep them unchanged."""
    from shutil import copy2

    for split in ["val", "test"]:
        src_split = os.path.join(INPUT_PATH, split)
        dst_split = os.path.join(OUTPUT_PATH, split)

        if not os.path.exists(src_split):
            print(f"[WARN] Split not found (skipping): {src_split}")
            continue

        print(f"\nCopying {split} split without augmentation...")
        for class_name in sorted(os.listdir(src_split)):
            src_class_dir = os.path.join(src_split, class_name)
            if not os.path.isdir(src_class_dir):
                continue

            dst_class_dir = os.path.join(dst_split, class_name)
            ensure_dir(dst_class_dir)

            for filename in os.listdir(src_class_dir):
                ext = os.path.splitext(filename)[1].lower()
                if ext not in IMAGE_EXTENSIONS:
                    continue
                src_path = os.path.join(src_class_dir, filename)
                dst_path = os.path.join(dst_class_dir, filename)
                copy2(src_path, dst_path)

        print(f"Finished copying {split} to {dst_split}")


def main():
    print("Starting augmentation...")
    ensure_dir(OUTPUT_PATH)

    process_train_split()
    copy_val_test()

    print("\nAll done! Augmented dataset is in:", OUTPUT_PATH)


if __name__ == "__main__":
    main()