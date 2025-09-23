import torch
import torch.nn as nn
import timm

class MultiLabelBackbone(nn.Module):
    def __init__(self, model_name: str = "convnext_tiny", num_classes: int = 200, pretrained: bool = True):
        super().__init__()
        self.backbone = timm.create_model(model_name, pretrained=pretrained, num_classes=0, global_pool="avg")
        in_features = getattr(self.backbone, "num_features", None)
        if in_features is None:
            raise ValueError("Backbone missing num_features")
        self.classifier = nn.Linear(in_features, num_classes)

    def forward(self, x):
        feats = self.backbone(x)
        logits = self.classifier(feats)
        return logits
