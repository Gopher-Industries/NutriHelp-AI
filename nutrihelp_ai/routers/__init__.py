# from .image_api import router as image_api
from .medical_report_api import router as medical_report_api
from .chatbot_api import router as chatbot_api
from .image_api import router as image_api
from .health_plan_api import router as health_plan_api
from .finetune_api import router as finetune_api

__all__ = ["medical_report_api", "chatbot_api", "image_api", "health_plan_api", "finetune_api"]
