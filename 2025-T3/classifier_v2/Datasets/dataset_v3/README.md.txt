# Dataset v3 – Food Image Classifier

## Overview
Dataset v3 is a forward-looking dataset structure prepared for future improvements to the NutriHelp food image classifier.
This version focuses on clean separation between training data and challenging edge cases, based on findings from classifier v2 stress testing.

No images are included at this stage. The structure is designed to support future data collection and retraining in the next trimester.


## Folder Structure
dataset_v3/
├── train/
│ └── <class folders>
├── val/
│ └── <class folders>
├── test/
│ └── <class folders>
├── stress_test/
│ ├── blur/
│ ├── cluttered_background/
│ ├── low_light/
│ ├── multi_food/
│ └── side_angle/
└── README.md


## Folder Descriptions

### train
Contains the main training images organised by food category.
These images should be clean, well-lit, and representative of typical user inputs.

### val
Validation dataset used to monitor model performance during training and prevent overfitting.

### test
Final evaluation dataset used to measure classifier accuracy after training is complete.

### stress_test
Contains intentionally challenging images used to evaluate model robustness.
Images in this folder are not used for training.

Stress test categories include:
- `blur` – motion blur or out-of-focus images
- `cluttered_background` – multiple objects or busy scenes
- `low_light` – dark or poorly lit images
- `multi_food` – multiple food items in one image
- `side_angle` – non-standard or angled viewpoints


## Purpose of Dataset v3

Dataset v3 was designed based on insights from classifier v2 stress testing.
Results showed reduced confidence and misclassification under challenging conditions.
This structure allows future teams to:
- Expand clean training data independently
- Systematically evaluate weaknesses
- Improve robustness without contaminating training data


## Future Work
- Populate training, validation, and test folders with curated images
- Gradually expand stress test cases
- Retrain classifier using Dataset v3
- Compare performance against classifier v2
