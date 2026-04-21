from typing import Dict, List, Literal, Optional

from pydantic import BaseModel, Field, field_validator

from .image_analysis import NutritionEstimate


MealType = Literal["Breakfast", "Lunch", "Dinner", "Snacks"]


class ScanMealLogCreate(BaseModel):
    user_id: Optional[str] = None
    date: Optional[str] = Field(
        default=None,
        description="YYYY-MM-DD. Defaults to today when omitted.",
    )
    meal_type: MealType = "Lunch"
    label: str = Field(..., min_length=1)
    confidence: float = Field(..., ge=0.0, le=1.0)
    estimated_calories: Optional[int] = Field(default=None, ge=0)
    serving_description: Optional[str] = None
    recommendation: str = ""
    is_unclear: bool = False
    quality_issues: List[str] = Field(default_factory=list)
    source: str = "scan"

    @field_validator("label", mode="before")
    def normalize_label(cls, value):
        return str(value).strip()


class MealLogEntry(BaseModel):
    id: str
    user_id: str
    date: str
    meal_type: MealType
    label: str
    confidence: float = Field(..., ge=0.0, le=1.0)
    estimated_calories: Optional[int] = Field(default=None, ge=0)
    serving_description: Optional[str] = None
    recommendation: str = ""
    is_unclear: bool = False
    quality_issues: List[str] = Field(default_factory=list)
    source: str = "scan"
    created_at: str


class DailyMealSummary(BaseModel):
    user_id: str
    date: str
    total_calories: int = Field(..., ge=0)
    entry_count: int = Field(..., ge=0)
    unclear_count: int = Field(..., ge=0)
    meal_type_breakdown: Dict[str, int] = Field(default_factory=dict)
    meals: List[MealLogEntry] = Field(default_factory=list)


class MealLogSaveResponse(BaseModel):
    entry: MealLogEntry
    daily_summary: DailyMealSummary


class NutritionPreviewResponse(NutritionEstimate):
    label: str


class MealChatContextResponse(BaseModel):
    user_id: str
    date: str
    has_data: bool
    summary: str
    prompt_context: str


class MealPlanContextResponse(BaseModel):
    user_id: str
    date_from: str
    date_to: str
    days: int = Field(..., ge=1)
    average_daily_calories: float = Field(..., ge=0.0)
    top_foods: List[str] = Field(default_factory=list)
    summary: str
    daily_summaries: List[DailyMealSummary] = Field(default_factory=list)
