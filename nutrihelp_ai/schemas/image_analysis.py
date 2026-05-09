from typing import List, Optional

from pydantic import BaseModel, Field


class LabelScore(BaseModel):
    label: str
    score: float = Field(..., ge=0.0, le=1.0)


class Top3Prediction(BaseModel):
    class_: str = Field(..., alias="class")
    confidence: float = Field(..., ge=0.0, le=1.0)


class ImageQuality(BaseModel):
    width: int = Field(..., ge=0)
    height: int = Field(..., ge=0)
    brightness: float = Field(..., ge=0.0, le=255.0)
    contrast: float = Field(..., ge=0.0)
    sharpness: float = Field(..., ge=0.0)
    passed: bool
    issues: List[str] = Field(default_factory=list)


class BaseImagePredictionResponse(BaseModel):
    label: Optional[str] = None
    confidence: float = Field(0.0, ge=0.0, le=1.0)
    confidence_tier: Optional[str] = None
    matches: List[LabelScore] = Field(default_factory=list)
    topk: List[LabelScore] = Field(default_factory=list)
    top3_predictions: List[Top3Prediction] = Field(default_factory=list)
    is_unclear: bool = False
    unclear_reason: str = ""
    retake_needed: bool = False
    retake_reason: Optional[str] = None
    suggestion: str = ""
    quality: ImageQuality
    error: Optional[str] = None


class NutritionEstimate(BaseModel):
    display_name: str = "Unknown Dish"
    about: Optional[str] = None
    cuisine: Optional[str] = None
    estimated_calories: Optional[int] = Field(default=None, ge=0)
    serving_description: Optional[str] = None
    source: str = "unavailable"
    available: bool = False


class SingleImageAnalysisResponse(BaseImagePredictionResponse):
    nutrition: NutritionEstimate
    recommendation: str = ""


class MultiImageAnalysisResponse(BaseModel):
    predictions: List[BaseImagePredictionResponse]
