import os

DATASET_PATH = "dataset_v2"   

# Add ALL common image formats
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp",".avif")

def count_images(folder_path):
    counts = {}
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return counts

    for class_name in sorted(os.listdir(folder_path)):
        class_folder = os.path.join(folder_path, class_name)
        if os.path.isdir(class_folder):
            num_images = len([
                f for f in os.listdir(class_folder)
                if f.lower().endswith(IMAGE_EXTENSIONS)
            ])
            counts[class_name] = num_images
    return counts

def print_counts(title, counts):
    print("\n" + title)
    print("-" * len(title))
    total = 0
    for cls, num in counts.items():
        print(f"{cls:<20} : {num}")
        total += num
    print(f"TOTAL: {total}")

train_counts = count_images(os.path.join(DATASET_PATH, "train"))
val_counts = count_images(os.path.join(DATASET_PATH, "val"))
test_counts = count_images(os.path.join(DATASET_PATH, "test"))  
print_counts("TRAIN SET", train_counts)
print_counts("VAL SET", val_counts)
print_counts("TEST SET", test_counts)  

