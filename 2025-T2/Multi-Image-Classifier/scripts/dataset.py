# dataset.py
import os
import json
import torch
from torch.utils.data import Dataset
from PIL import Image
import pandas as pd

class VFNDataset(Dataset):
    def __init__(self, csv_file, classes_file, transform=None):
        self.data = pd.read_csv(csv_file)
        with open(classes_file, "r") as f:
            self.classes = json.load(f)
        self.transform = transform
        self.num_classes = len(self.classes)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        image = Image.open(row["image"]).convert("RGB")

        if self.transform:
            image = self.transform(image)

        label_vector = torch.zeros(self.num_classes, dtype=torch.float32)
        for lbl in json.loads(row["labels"]): 
            label_vector[lbl] = 1.0

        return image, label_vector
