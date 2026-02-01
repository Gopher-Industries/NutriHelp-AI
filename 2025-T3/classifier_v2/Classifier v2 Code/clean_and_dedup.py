import os
from PIL import Image
import imagehash

def clean_and_dedup(folder, min_size=200, ratio_limit=3, dup_threshold=5):
    hashes = {}
    removed_bad = 0
    removed_dup = 0

    for f in os.listdir(folder):
        path = os.path.join(folder, f)

        # Skip subfolders just in case
        if not os.path.isfile(path):
            continue

        try:
            img = Image.open(path).convert("RGB")
            w, h = img.size

            # 1️⃣ Remove tiny images
            if w < min_size or h < min_size:
                os.remove(path)
                removed_bad += 1
                continue

            # 2️⃣ Remove extreme aspect ratios
            if w / h > ratio_limit or h / w > ratio_limit:
                os.remove(path)
                removed_bad += 1
                continue

            # 3️⃣ Duplicate detection (perceptual hash)
            hsh = imagehash.phash(img)

            for existing_hsh in hashes:
                if abs(hsh - existing_hsh) <= dup_threshold:
                    os.remove(path)
                    removed_dup += 1
                    break
            else:
                hashes[hsh] = path

        except:
            os.remove(path)
            removed_bad += 1

    print(
        f"{os.path.basename(folder):20s} | "
        f"bad: {removed_bad:4d} | "
        f"dup: {removed_dup:4d} | "
        f"kept: {len(hashes):4d}"
    )

# ▶ MAIN: run for all classes
BASE_DIR = "western_variety_images"

print("Cleaning and deduplicating dataset...\n")

for cls in os.listdir(BASE_DIR):
    class_path = os.path.join(BASE_DIR, cls)
    if os.path.isdir(class_path):
        clean_and_dedup(class_path)

print("\nDone.")