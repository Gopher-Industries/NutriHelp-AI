from icrawler.builtin import BingImageCrawler
import os

# Each class has multiple query prompts for variety
queries = {
    "burger": [
        "cheeseburger meal photo",
        "burger on plate photo",
        "fast food burger photo",
        "burger close up photo"
    ],
    "pizza": [
        "pepperoni pizza slice photo",
        "margherita pizza top view",
        "pizza in box photo",
        "pizza on wooden board photo"
    ],
    "pasta": [
        "spaghetti bolognese plate photo",
        "pasta carbonara photo",
        "penne alfredo photo",
        "pasta in restaurant photo"
    ],
    "steak": [
        "grilled steak on plate photo",
        "steak and fries photo",
        "medium rare steak sliced photo",
        "steak dinner photo"
    ],
    "fish_and_chips": [
        "fish and chips on plate photo",
        "fish and chips takeaway photo",
        "fish and chips close up photo"
    ],
    "tacos": [
        "beef tacos photo",
        "street tacos on tray photo",
        "tacos close up photo"
    ],
    "burrito": [
        "burrito wrap cut in half photo",
        "breakfast burrito photo",
        "burrito in foil photo"
    ],
    "pancakes": [
        "pancakes stack syrup photo",
        "pancakes on plate photo",
        "blueberry pancakes photo"
    ],
    "donut": [
        "glazed donut photo",
        "donuts box photo",
        "chocolate donut close up photo"
    ],
    "fries": [
        "french fries photo",
        "loaded fries photo",
        "fries in basket photo"
    ],
    "wings": [
        "chicken wings platter photo",
        "buffalo wings photo",
        "bbq wings close up photo"
    ],
    "nachos": [
        "nachos cheese photo",
        "nachos with guacamole photo",
        "loaded nachos photo"
    ],
    "caesar_salad": [
        "caesar salad bowl photo",
        "chicken caesar salad photo",
        "caesar salad close up photo"
    ],
    "sandwich": [
        "club sandwich photo",
        "turkey sandwich on plate photo",
        "sandwich meal photo"
    ]
}

BASE_DIR = "western_variety_images"
IMAGES_PER_QUERY = 120  # 120 x 3-4 prompts ≈ 360-480 images per class

os.makedirs(BASE_DIR, exist_ok=True)

for label, qlist in queries.items():
    folder = os.path.join(BASE_DIR, label)
    os.makedirs(folder, exist_ok=True)

    for q in qlist:
        print(f"[{label}] Downloading: {q}")
        crawler = BingImageCrawler(storage={'root_dir': folder})
        crawler.crawl(
            keyword=q,
            max_num=IMAGES_PER_QUERY,
            filters={'type': 'photo', 'size': 'large'}
        )

print("Done.")