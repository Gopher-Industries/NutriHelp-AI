# Dataset v2 – Augmented (Experimental)

## Purpose
This dataset contains **augmented versions of Dataset v2** created during
**Trimester 3, 2025** to improve robustness of the experimental Classifier v2.

The goal of augmentation was to simulate real-world image variability without
collecting additional raw data.

---

## Source Dataset
- Base dataset: `dataset_v2/`
- Created for: Classifier v2 experimentation
- Scope: Research and evaluation only (not production)

---

## Augmentation Techniques Applied
Augmentation was applied **only to the training split**.

Techniques include:
- Random rotations
- Horizontal flips
- Brightness adjustments
- Minor contrast variations

These augmentations were chosen to improve tolerance to:
- Lighting variation
- Camera angle differences
- Minor image noise

---

## Dataset Characteristics
- Same class set as `dataset_v2`
- Increased sample count via synthetic augmentation
- Validation and test sets remain **unaugmented** to preserve evaluation integrity

---

## Notes
- Augmented images are **not uploaded** to the repository due to size constraints
- Dataset is used exclusively for experimental training
- Results are documented in evaluation artifacts and notebooks

This dataset exists to support learning and analysis, not deployment.
