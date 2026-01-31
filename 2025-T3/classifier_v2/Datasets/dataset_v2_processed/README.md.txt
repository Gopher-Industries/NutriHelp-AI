# Dataset v2 – Processed (Experimental)

## Purpose
This dataset contains **fully preprocessed images** derived from `dataset_v2`
for training and evaluating the experimental Classifier v2 during **T3 2025**.

Processing ensures consistency across all images before model ingestion.

---

## Processing Steps Applied
All images underwent the following preprocessing steps:

- File format standardisation (PNG / WEBP → JPG)
- Image resizing to **224 × 224**
- RGB colour enforcement
- Removal of corrupted or invalid files
- Filtering of extreme aspect ratios
- Deduplication checks

---

## Dataset Characteristics
- Same class labels as `dataset_v2`
- Cleaned and normalised input data
- Ready for direct use in training pipelines

---

## Usage
This dataset was used for:
- Controlled training experiments
- Reproducible evaluation
- Stress testing classifier behaviour

---

## Notes
- Processed images are **not committed** to the repository
- Only metadata, scripts, and evaluation results are tracked
- Dataset exists to document preprocessing decisions and workflow

This supports transparency without bloating the repository.
