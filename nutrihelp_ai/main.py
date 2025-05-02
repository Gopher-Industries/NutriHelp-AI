# main.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from nutrihelp_ai.routers import image_api, obesity_api, chatbot_api, diabetes_api
from nutrihelp_ai.extensions import limiter

import logging
from slowapi.errors import RateLimitExceeded
from slowapi.extension import _rate_limit_exceeded_handler

# ---- Logging Setup ----
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("nutrihelp")

# ---- FastAPI App ----
app = FastAPI(
    title="NutriHelp AI API",
    description="API for AI models",
    version="1.0"
)

# ---- Attach Limiter ----
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# ---- Register Routers ----
app.include_router(image_api, prefix="/ai-model/image", tags=["Image Classification"])
app.include_router(obesity_api, prefix="/ai-model/obesity", tags=["Obesity Prediction"])
app.include_router(chatbot_api, prefix="/ai-model/chatbot", tags=["AI Assistant"])
app.include_router(diabetes_api, prefix="/ai-model/diabetes", tags=["Diabetes Prediction"])

# ---- Custom Error Handlers ----
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    logger.warning(f"HTTP Error: {exc.detail} at {request.url}")
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning(f"Validation Error: {exc.errors()} at {request.url}")
    return JSONResponse(status_code=422, content={"error": "Invalid request", "details": exc.errors()})

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unexpected error at {request.url}: {repr(exc)}")
    return JSONResponse(status_code=500, content={"error": "Internal server error"})
