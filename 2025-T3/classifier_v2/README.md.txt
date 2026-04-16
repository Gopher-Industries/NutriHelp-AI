# ai_evaluation – Classifier Experiments & Evaluation (T3 2025)

## Experimental Work – T3 2025 Evidence Only

This folder documents **experimental classifier development and evaluation**
conducted during **Trimester 3, 2025** as part of the NutriHelp AI team work.

The contents in this folder are **NOT used in production**  
They are preserved **for learning, evaluation, and assessment evidence**

---

## Overview

This directory contains **experimental work, evaluations, and research artifacts**
related to food image classification in the NutriHelp AI project.

The purpose of this folder is to clearly separate:
- **Research and experimentation**
- **Evaluation-driven decision making**
from
- **Production-safe backend improvements**

---

## Folder Purpose

The goals of this folder are to:
- Explore potential improvements to food image classification
- Experiment with a new classifier version (Classifier v2)
- Analyse misclassifications and dataset limitations
- Provide evidence to support backend and architectural decisions

---

## Classifier v2  
### (Experimental – Not Integrated into Production)

Classifier v2 was developed during **Weeks 3–7 (T3 2025)** as an experimental attempt
to improve food image classification accuracy.

### Key Characteristics
- Trained using custom-collected and augmented image datasets
- Focused on increasing food variety coverage and robustness
- Evaluated using curated evaluation sets and stress testing

### Outcome

Although multiple training iterations were conducted, **Classifier v2 did not
outperform the existing production classifier** due to:

- Limited access to the original full image dataset
- Class imbalance and insufficient data for certain food categories
- Increased regression risk if deployed

As a result, **Classifier v2 was deliberately not integrated into the backend** and
is retained here strictly for documentation, evaluation, and learning purposes.

---

## Production-Safe Backend Improvements

Instead of replacing the existing model, improvements were applied at the
**backend pipeline level**, which is safer and aligns with system stability goals.

### Implemented Enhancements
- Multi-image classification support
- Explicit confidence score extraction
- Top-K prediction handling
- Automatic detection of *unclear images*
- User-facing feedback:
  > **“Please upload a clearer image”** when confidence is low

### Relevant Production Files
- `nutrihelp_ai/services/multi_image_pipeline.py`
- `nutrihelp_ai/routers/multi_image_api.py`

These changes improve reliability **without retraining or replacing the production model**.

---

## Evaluation & Results

The evaluation artifacts include:

- `evaluation_set/`
  - `asian/`
  - `western/`
  - `mixed/`
  - `unclear/`
- `image_classification_results.xlsx`

The evaluation spreadsheet records:
- Image name
- Expected food category
- Predicted label(s)
- Confidence scores
- Unclear-image flags

This data was used to analyse:
- Performance consistency across food styles
- Confidence behaviour on ambiguous inputs
- Failure cases caused by missing or underrepresented classes

---

## Dataset Versioning

All datasets are **explicitly versioned** to ensure traceability and reproducibility:

- `dataset_v2/`
- `dataset_v2_augmented/`
- `dataset_v2_processed/`
- `dataset_v3/`

Each dataset version reflects different preprocessing or augmentation strategies
explored during the trimester.

---

## Final Notes

This folder documents **exploration, evaluation, and decision-making**, not only
successful outcomes.

**Key takeaway:**  
Rather than deploying a weaker experimental model, overall system reliability
was improved through **confidence-aware backend logic** and safer architectural changes.

Future improvements depend on access to a **complete, well-balanced image dataset**.
