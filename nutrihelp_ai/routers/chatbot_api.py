from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field
from datetime import datetime
from nutrihelp_ai.services.active_ai_backend import GroqChromaBackend

import uuid

router = APIRouter()
agent = GroqChromaBackend()

class ChatRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=1,
        max_length=2000,           
        strip_whitespace=True,
        description="User's chat message or question"
    )

class ChatResponse(BaseModel):
    status: str = "success"
    msg: str
    id: str
    timestamp: str

class ErrorResponse(BaseModel):
    status: str = "error"          
    error: str
    detail: str | None = None
    timestamp: str

@router.post("/chat", response_model=ChatResponse)
def sync_chat(request: ChatRequest):
    try:
        msg = agent.chat_with_rag_fallback(request.query)
        unique_id = str(uuid.uuid4())
        return ChatResponse(
            msg=msg,
            id=unique_id,
            timestamp=datetime.now().isoformat()
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=ErrorResponse(                  
                error="Internal Server Error",
                detail=str(e),
                timestamp=datetime.now().isoformat()
            ).dict()
        )
    
@router.post("/chat_with_rag", response_model=ChatResponse)
def sync_chat(request: ChatRequest):
    try:
        msg = agent.generate_with_rag(request.query)
        unique_id = str(uuid.uuid4())
        return ChatResponse(
            msg=msg,
            id=unique_id,
            timestamp=datetime.now().isoformat()
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=ErrorResponse(                  
                error="Internal Server Error",
                detail=str(e),
                timestamp=datetime.now().isoformat()
            ).dict()
        )