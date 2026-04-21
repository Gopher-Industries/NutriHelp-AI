import json
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path
from threading import Lock
from typing import Any, Dict, List, Optional
from uuid import uuid4

from nutrihelp_ai.schemas.meal_log import (
    DailyMealSummary,
    MealChatContextResponse,
    MealLogEntry,
    MealPlanContextResponse,
    ScanMealLogCreate,
)
from nutrihelp_ai.services.nutrition_lookup import NutritionLookupService


class MealLogService:
    def __init__(self, data_path: Optional[Path] = None):
        self.data_path = data_path or Path(__file__).resolve().parent.parent / "data" / "meal_logs.json"
        self._lock = Lock()
        self.nutrition_lookup = NutritionLookupService()
        self._ensure_file()

    def create_entry(self, payload: ScanMealLogCreate) -> MealLogEntry:
        entry_date = self._normalize_date(payload.date)
        user_id = self._normalize_user_id(payload.user_id)

        nutrition = self.nutrition_lookup.lookup(payload.label)
        estimated_calories = payload.estimated_calories
        if estimated_calories is None:
            estimated_calories = nutrition.get("estimated_calories")

        serving_description = payload.serving_description
        if not serving_description:
            serving_description = nutrition.get("serving_description")

        entry = MealLogEntry(
            id=str(uuid4()),
            user_id=user_id,
            date=entry_date,
            meal_type=payload.meal_type,
            label=payload.label,
            confidence=payload.confidence,
            estimated_calories=estimated_calories,
            serving_description=serving_description,
            recommendation=payload.recommendation,
            is_unclear=payload.is_unclear,
            quality_issues=list(payload.quality_issues),
            source=payload.source,
            created_at=datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        )

        with self._lock:
            entries = self._load_entries()
            entries.append(entry.model_dump())
            self._save_entries(entries)

        return entry

    def delete_entry(self, entry_id: str, user_id: Optional[str] = None) -> bool:
        normalized_user = self._normalize_user_id(user_id)
        with self._lock:
            entries = self._load_entries()
            next_entries = []
            deleted = False
            for raw in entries:
                if raw.get("id") == entry_id and raw.get("user_id") == normalized_user:
                    deleted = True
                    continue
                next_entries.append(raw)
            if deleted:
                self._save_entries(next_entries)
            return deleted

    def list_entries(
        self,
        *,
        target_date: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> List[MealLogEntry]:
        normalized_user = self._normalize_user_id(user_id)
        normalized_date = self._normalize_date(target_date) if target_date else None
        entries = [
            MealLogEntry(**raw)
            for raw in self._load_entries()
            if raw.get("user_id") == normalized_user
            and (normalized_date is None or raw.get("date") == normalized_date)
        ]
        entries.sort(key=lambda item: (item.date, item.created_at, item.id), reverse=True)
        return entries

    def get_daily_summary(
        self,
        *,
        target_date: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> DailyMealSummary:
        normalized_user = self._normalize_user_id(user_id)
        normalized_date = self._normalize_date(target_date)
        meals = self.list_entries(target_date=normalized_date, user_id=normalized_user)
        total_calories = sum(int(item.estimated_calories or 0) for item in meals)
        unclear_count = sum(1 for item in meals if item.is_unclear)
        meal_type_breakdown = {meal_type: 0 for meal_type in ("Breakfast", "Lunch", "Dinner", "Snacks")}
        for item in meals:
            meal_type_breakdown[item.meal_type] = meal_type_breakdown.get(item.meal_type, 0) + 1

        return DailyMealSummary(
            user_id=normalized_user,
            date=normalized_date,
            total_calories=total_calories,
            entry_count=len(meals),
            unclear_count=unclear_count,
            meal_type_breakdown=meal_type_breakdown,
            meals=meals,
        )

    def build_chat_context(
        self,
        *,
        target_date: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> MealChatContextResponse:
        summary = self.get_daily_summary(target_date=target_date, user_id=user_id)
        if not summary.meals:
            return MealChatContextResponse(
                user_id=summary.user_id,
                date=summary.date,
                has_data=False,
                summary="No meals have been logged for that day.",
                prompt_context="",
            )

        meal_lines = []
        for item in summary.meals[:8]:
            calories_text = (
                f"{item.estimated_calories} kcal"
                if item.estimated_calories is not None
                else "calories unavailable"
            )
            meal_lines.append(
                f"- {item.meal_type}: {item.label} ({calories_text}, confidence {item.confidence:.2f})"
            )

        summary_text = (
            f"On {summary.date}, the user logged {summary.entry_count} meals totaling "
            f"about {summary.total_calories} kcal."
        )
        prompt_context = (
            "Use the following logged meals as recent dietary context. "
            "Treat calorie values as rough estimates, not exact nutrition facts.\n"
            f"Meal date: {summary.date}\n"
            + "\n".join(meal_lines)
        )
        return MealChatContextResponse(
            user_id=summary.user_id,
            date=summary.date,
            has_data=True,
            summary=summary_text,
            prompt_context=prompt_context,
        )

    def build_plan_context(
        self,
        *,
        user_id: Optional[str] = None,
        date_to: Optional[str] = None,
        days: int = 7,
    ) -> MealPlanContextResponse:
        normalized_user = self._normalize_user_id(user_id)
        end_date = datetime.strptime(self._normalize_date(date_to), "%Y-%m-%d").date()
        safe_days = max(1, int(days))
        start_date = end_date - timedelta(days=safe_days - 1)

        daily_summaries: List[DailyMealSummary] = []
        food_counter: Counter[str] = Counter()
        total_calories = 0
        logged_days = 0

        for offset in range(safe_days):
            current = (start_date + timedelta(days=offset)).isoformat()
            summary = self.get_daily_summary(target_date=current, user_id=normalized_user)
            daily_summaries.append(summary)
            if summary.entry_count > 0:
                logged_days += 1
                total_calories += summary.total_calories
                food_counter.update(item.label for item in summary.meals)

        average = total_calories / logged_days if logged_days else 0.0
        top_foods = [label for label, _ in food_counter.most_common(5)]
        summary_text = (
            f"Over the last {safe_days} day(s), the user logged meals on {logged_days} day(s) "
            f"with an average of {average:.1f} kcal on logged days."
        )

        return MealPlanContextResponse(
            user_id=normalized_user,
            date_from=start_date.isoformat(),
            date_to=end_date.isoformat(),
            days=safe_days,
            average_daily_calories=round(average, 1),
            top_foods=top_foods,
            summary=summary_text,
            daily_summaries=daily_summaries,
        )

    def _ensure_file(self):
        self.data_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.data_path.exists():
            self.data_path.write_text("[]", encoding="utf-8")

    def _load_entries(self) -> List[Dict[str, Any]]:
        try:
            return json.loads(self.data_path.read_text(encoding="utf-8"))
        except Exception:
            return []

    def _save_entries(self, entries: List[Dict[str, Any]]):
        self.data_path.write_text(json.dumps(entries, indent=2), encoding="utf-8")

    def _normalize_user_id(self, user_id: Optional[str]) -> str:
        value = (user_id or "anonymous").strip()
        return value or "anonymous"

    def _normalize_date(self, value: Optional[str]) -> str:
        if not value:
            return date.today().isoformat()
        return datetime.strptime(value, "%Y-%m-%d").date().isoformat()
