# nutrihelp_ai/routers/finetune_api.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Literal, Optional, Dict, Any
import os, httpx, asyncio
from datetime import datetime

router = APIRouter()

HF_SPACE_URL = os.getenv("HF_SPACE_URL", "https://ngtuanphong-nutribot.hf.space").rstrip("/")
HF_SPACE_KEY = os.getenv("HF_SPACE_KEY", "").strip()
HEADERS = {"Authorization": f"Bearer {HF_SPACE_KEY}"} if HF_SPACE_KEY else {}

# one shared AsyncClient with a generous timeout
CLIENT = httpx.AsyncClient(
    timeout=httpx.Timeout(180.0, connect=30.0),  # 3 min total, 30s connect
    limits=httpx.Limits(max_keepalive_connections=10, max_connections=20),
    follow_redirects=True,
)

class ChatMessage(BaseModel):
    role: Literal["system","user","assistant"]
    content: str

class ErrorResponse(BaseModel):
    status: str = "error"
    error: str
    detail: str | None = None
    timestamp: str

class ChatCompletionRequest(BaseModel):
    model: Optional[str] = None
    messages: List[ChatMessage]
    max_tokens: int = 256
    temperature: float = 0.7
    top_p: float = 0.9
    repetition_penalty: float = 1.05

async def _retry_post(url: str, json: Dict[str, Any], headers: Dict[str, str], tries: int = 3) -> httpx.Response:
    delay = 1.5
    last_exc: Exception | None = None
    for attempt in range(1, tries + 1):
        try:
            return await CLIENT.post(url, json=json, headers=headers)
        except (httpx.ReadTimeout, httpx.ConnectTimeout, httpx.RemoteProtocolError) as e:
            last_exc = e
            if attempt == tries:
                raise HTTPException(
                    status_code=504,
                    detail=f"Failed after {tries} attempts. Last error: {type(last_exc).__name__}"
                )
            await asyncio.sleep(delay)
            delay *= 2  # backoff

@router.get("/healthz")
async def healthz():
    # Try the Space /healthz
    try:
        resp = await CLIENT.get(f"{HF_SPACE_URL}/healthz", headers=HEADERS)
        ok = resp.status_code == 200
        body = {}
        try:
            body = resp.json()
        except Exception:
            body = {"raw": resp.text[:200]}
        return {"ok": ok, "space_status": resp.status_code, "space_health": body, "space_url": HF_SPACE_URL}
    except Exception as e:
        raise HTTPException(
            status_code=502, 
            detail=ErrorResponse(
                status="error",
                error="Cannot reach Space",
                detail=f"{type(e).__name__}: {e}",
                timestamp=datetime.now().isoformat()
            ).dict()
        )

@router.post("/chat")
async def finetune_chat(req: ChatCompletionRequest) -> Dict[str, Any]:
    # optional preflight to wake the Space on first call
    try:
        await CLIENT.get(f"{HF_SPACE_URL}/healthz", headers=HEADERS)
    except Exception:
        pass  # non-fatal

    try:
        # forward to your Space chat endpoint
        resp = await _retry_post(f"{HF_SPACE_URL}/v1/chat/completions", req.dict(), HEADERS)
        resp.raise_for_status()
        return resp.json()
    
    except httpx.HTTPStatusError as e:
        # bubble up Space errors with its body (useful for debugging)
        text = e.response.text
        raise HTTPException(
            status_code=e.response.status_code,
            detail=ErrorResponse(
                status="error",
                error="Space error",
                detail=f"{text[:500]}{'…' if len(text) > 500 else ''}",
                timestamp=datetime.now().isoformat()
            ).dict()
        )
    
    except (httpx.ReadTimeout, httpx.ConnectTimeout) as e:
        # translate network timeouts into 504 for the client
        raise HTTPException(
            status_code=504, 
            detail=ErrorResponse(
                status="error",
                error="Gateway timeout reaching Space",
                detail=f"{type(e).__name__}: {e}",
                timestamp=datetime.now().isoformat()
            ).dict()
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=502, 
            detail=ErrorResponse(
                status="error",
                error="Upstream error reaching Space",
                detail=f"{type(e).__name__}: {e}",
                timestamp=datetime.now().isoformat()
            ).dict()
        )
