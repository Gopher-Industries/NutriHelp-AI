# README for NutriHelp-AI dataset_v2

This dataset (v2) was created as part of the T3 2025 NutriHelp Capstone project to support future improvements to the food image classifier.
It contains cleaned, curated, and organised food images grouped into 15 food categories.

Dataset v2 is designed for:

* Improved training stability
* Better class balance
* Higher-quality food images
* Clearer visual boundaries between categories
* Future retraining in T1 2026


## Folder Structure

The dataset follows a standard machine-learning structure:

```
dataset_v2/
   train/
      <15 class folders>
   val/
      <15 class folders>
   test/
      <15 class folders>
   README.md
```

Each folder contains the same set of classes.


## Food Classes Included

1. Beef
2. Bread
3. Chicken
4. Egg
5. Fruit
6. Lamb
7. Noodles
8. Pasta
9. Pork
10. Rice
11. Salad
12. Seafood
13. Snacks
14. Soups
15. Vegetables


## Image Counts & Splits

Images were split using a 70/20/10 train–val–test ratio:

| Class      | Total | Train | Val | Test |
| ---------- | ----- | ----- | --- | ---- |
| Beef       | 6     | 4     | 1   | 1    |
| Bread      | 11    | 8     | 2   | 1    |
| Chicken    | 29    | 20    | 6   | 3    |
| Egg        | 9     | 6     | 2   | 1    |
| Fruits     | 11    | 8     | 2   | 1    |
| Lamb       | 5     | 3     | 1   | 1    |
| Noodles    | 20    | 14    | 4   | 2    |
| Pasta      | 12    | 8     | 2   | 2    |
| Pork       | 6     | 4     | 1   | 1    |
| Rice       | 19    | 13    | 4   | 2    |
| Salad      | 16    | 11    | 3   | 2    |
| Seafood    | 12    | 8     | 2   | 2    |
| Snacks     | 16    | 11    | 3   | 2    |
| Soups      | 22    | 15    | 4   | 3    |
| Vegetables | 14    | 10    | 3   | 1    |


## Data Cleaning Process

All raw images were manually inspected and cleaned:

* Removed low-resolution / pixelated images
* Removed images with watermarks, text, advertisements
* Removed irrelevant backgrounds
* Cropped to focus on the food item
* Ensured the main food object is clear and visible
* Removed duplicate or near-duplicate images


## Image Preprocessing

Minimal preprocessing was performed:

* Images were cropped to remove distractions
* No resizing was done (resizing will be handled during model training)
* Mixed formats (JPG, PNG, WEBP) are preserved and acceptable


## Purpose of Dataset v2

* Provide a cleaner, better-structured dataset for future classifier retraining
* Address misclassification issues found in Week 3 evaluation
* Expand under-represented classes
* Support the Capstone team in developing Classifier v2 in T1 2026


## Versioning

* Dataset v2 (current): cleaned, expanded, and split dataset
* Dataset v3 (future): improvements recommended for T1 2026


