import os
from PIL import Image

# ==== CONFIG ====
DATASET_PATH = "dataset_v2"              # input folder
OUTPUT_PATH = "dataset_v2_processed"     # output folder
TARGET_SIZE = (224, 224)                 # (width, height)

IMAGE_EXTENSIONS =  (".jpg", ".jpeg", ".png", ".webp",".avif")
# =================


def ensure_dir(path: str):
    """Create folder if it doesn't exist."""
    os.makedirs(path, exist_ok=True)


def process_image(input_path: str, output_path: str):
    """Open, convert, resize and save image as .jpg."""
    try:
        with Image.open(input_path) as img:
            # Convert to RGB to avoid issues with PNG/WEBP with alpha
            img = img.convert("RGB")
            img = img.resize(TARGET_SIZE)

            # Always save as .jpg
            ensure_dir(os.path.dirname(output_path))
            img.save(output_path, format="JPEG", quality=90)
            return True
    except Exception as e:
        print(f"  [SKIP] Failed to process {input_path}: {e}")
        return False


def process_split(split_name: str):
    """Process one of: train / val / test."""
    input_split_dir = os.path.join(DATASET_PATH, split_name)
    output_split_dir = os.path.join(OUTPUT_PATH, split_name)

    if not os.path.exists(input_split_dir):
        print(f"[WARN] Split folder not found: {input_split_dir}")
        return

    print(f"\n=== Processing split: {split_name} ===")

    total_files = 0
    processed_files = 0
    skipped_files = 0

    for class_name in sorted(os.listdir(input_split_dir)):
        input_class_dir = os.path.join(input_split_dir, class_name)
        if not os.path.isdir(input_class_dir):
            continue

        output_class_dir = os.path.join(output_split_dir, class_name)
        ensure_dir(output_class_dir)

        print(f"\nClass: {class_name}")
        for filename in os.listdir(input_class_dir):
            total_files += 1
            ext = os.path.splitext(filename)[1].lower().strip()

            # Skip files with no/unsupported extension
            if ext not in IMAGE_EXTENSIONS:
                skipped_files += 1
                print(f"  [SKIP] {filename} (unsupported extension: {ext})")
                continue

            input_path = os.path.join(input_class_dir, filename)

            # Build output filename (same name but .jpg)
            base_name = os.path.splitext(filename)[0]
            output_filename = base_name + ".jpg"
            output_path = os.path.join(output_class_dir, output_filename)

            ok = process_image(input_path, output_path)
            if ok:
                processed_files += 1
            else:
                skipped_files += 1

    print(f"\nSummary for {split_name}:")
    print(f"  Total files seen     : {total_files}")
    print(f"  Successfully processed: {processed_files}")
    print(f"  Skipped / failed     : {skipped_files}")


def main():
    print("Starting preprocessing...")
    ensure_dir(OUTPUT_PATH)

    for split in ["train", "val", "test"]:
        process_split(split)

    print("\nAll done! Processed dataset is in:", OUTPUT_PATH)


if __name__ == "__main__":
    main()
