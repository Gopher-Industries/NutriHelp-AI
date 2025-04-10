from .image_api import router as image_api
from .obesity_api import router as obesity_api
from .chatbot_api import router as chatbot_api

__all__ = ["image_api", "obesity_api", "chatbot_api"]
