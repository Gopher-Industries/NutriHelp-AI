from slowapi.extension import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
import logging
from nutrihelp_ai.extensions import limiter
from nutrihelp_ai.routers import multi_image_api  # NEW: Multi-image router
from nutrihelp_ai.routers import medical_report_api, chatbot_api, image_api, health_plan_api, finetune_api
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request
from nutrihelp_ai.routers import classifier_v2
from nutrihelp_ai.routers import mealplan_api
from dotenv import load_dotenv
import os

# Load .env file before anything else
load_dotenv()


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

# ---- Allow all origins (for development) ----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Attach Limiter ----
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# ---- Health Check ----


@app.api_route("y", methods=["GET", "HEAD"])
async def root():
    return JSONResponse(status_code=200, content={"status": "ok"})


@app.get("/healthz")
async def healthz():
    return JSONResponse(status_code=200, content={"status": "ok"})

# ---- Register Routers ----
app.include_router(medical_report_api, prefix="/ai-model/medical-report",
                   tags=["Medical Report Generation"])
app.include_router(chatbot_api, prefix="/ai-model/chatbot",
                   tags=["AI Assistant"])
app.include_router(image_api, prefix="/ai-model/image-analysis",
                   tags=["Image classification"])

app.include_router(multi_image_api.router, prefix="/ai-model/image-analysis",
                   tags=["Multi Image Classification"])

app.include_router(health_plan_api, prefix="/ai-model/medical-report/plan",
                   tags=["Health Plan Generation"])
app.include_router(finetune_api, prefix="/ai-model/chatbot-finetune",
                   tags=["AI Assistant Fine tune"])

app.include_router(classifier_v2.router)
app.include_router(mealplan_api.router)

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
