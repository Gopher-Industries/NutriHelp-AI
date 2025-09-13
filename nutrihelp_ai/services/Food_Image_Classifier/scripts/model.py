import torch
import torch.nn as nn
from torchvision.models import efficientnet_b0, EfficientNet_B0_Weights

class FoodClassifier(nn.Module):
    def __init__(self, num_classes=101):
        super(FoodClassifier, self).__init__()
        weights = EfficientNet_B0_Weights.IMAGENET1K_V1
        self.base_model = efficientnet_b0(weights=weights)
        in_features = self.base_model.classifier[1].in_features
        self.base_model.classifier = nn.Sequential(
            nn.Dropout(0.3),
            nn.Linear(in_features, num_classes)
        )

    def forward(self, x):
        return self.base_model(x)