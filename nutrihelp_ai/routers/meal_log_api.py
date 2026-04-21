import logging
from datetime import date
from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from nutrihelp_ai.schemas import (
    DailyMealSummary,
    MealChatContextResponse,
    MealLogEntry,
    MealLogSaveResponse,
    MealPlanContextResponse,
    NutritionPreviewResponse,
    ScanMealLogCreate,
)
from nutrihelp_ai.services.meal_log_service import MealLogService
from nutrihelp_ai.services.nutrition_lookup import NutritionLookupService


logger = logging.getLogger(__name__)
router = APIRouter()
service = MealLogService()
nutrition_lookup = NutritionLookupService()


@router.post("/log-scan", response_model=MealLogSaveResponse, summary="Save scanned meal")
async def save_scanned_meal(payload: ScanMealLogCreate):
    try:
        entry = service.create_entry(payload)
        summary = service.get_daily_summary(target_date=entry.date, user_id=entry.user_id)
        return MealLogSaveResponse(entry=entry, daily_summary=summary)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception as exc:
        logger.error("Failed to save scanned meal: %s", exc, exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to save meal log entry.")


@router.get(
    "/nutrition-preview",
    response_model=NutritionPreviewResponse,
    summary="Preview rough calories for a confirmed label",
)
async def get_nutrition_preview(label: str = Query(..., min_length=1)):
    normalized_label = label.strip()
    if not normalized_label:
        raise HTTPException(status_code=400, detail="Label is required.")

    preview = nutrition_lookup.lookup(normalized_label)
    return NutritionPreviewResponse(label=normalized_label, **preview)


@router.get("/logs", response_model=List[MealLogEntry], summary="List meal logs")
async def list_meal_logs(
    date_value: Optional[date] = Query(default=None, alias="date"),
    user_id: Optional[str] = Query(default=None),
):
    try:
        normalized = date_value.isoformat() if date_value else None
        return service.list_entries(target_date=normalized, user_id=user_id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.delete("/logs/{entry_id}", summary="Delete meal log")
async def delete_meal_log(entry_id: str, user_id: Optional[str] = Query(default=None)):
    deleted = service.delete_entry(entry_id, user_id=user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Meal log entry not found.")
    return {"deleted": True, "entry_id": entry_id}


@router.get("/daily-summary", response_model=DailyMealSummary, summary="Get daily meal summary")
async def get_daily_summary(
    date_value: Optional[date] = Query(default=None, alias="date"),
    user_id: Optional[str] = Query(default=None),
):
    try:
        normalized = date_value.isoformat() if date_value else None
        return service.get_daily_summary(target_date=normalized, user_id=user_id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.get("/chat-context", response_model=MealChatContextResponse, summary="Build chat context from meals")
async def get_chat_context(
    date_value: Optional[date] = Query(default=None, alias="date"),
    user_id: Optional[str] = Query(default=None),
):
    try:
        normalized = date_value.isoformat() if date_value else None
        return service.build_chat_context(target_date=normalized, user_id=user_id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.get("/plan-context", response_model=MealPlanContextResponse, summary="Build meal-plan context")
async def get_plan_context(
    date_to: Optional[date] = Query(default=None),
    days: int = Query(default=7, ge=1, le=30),
    user_id: Optional[str] = Query(default=None),
):
    try:
        normalized_date = date_to.isoformat() if date_to else None
        return service.build_plan_context(user_id=user_id, date_to=normalized_date, days=days)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
