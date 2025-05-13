# from .image_api import router as image_api
from .medical_report_api import router as medical_report_api
from .chatbot_api import router as chatbot_api

__all__ = ["medical_report_api", "chatbot_api"]
