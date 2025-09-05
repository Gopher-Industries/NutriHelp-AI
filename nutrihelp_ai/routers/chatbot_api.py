# chatbot_api.py
from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from nutrihelp_ai.services.nutribot.Agents import AgentClass

import uuid

router = APIRouter()

class UserInput(BaseModel):
    Input: str

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    msg: str
    id: str


@router.post("/chat", response_model=ChatResponse)
def sync_chat(request: ChatRequest, background_tasks: BackgroundTasks):
    try:
        agent = AgentClass()
        msg = agent.run_agent(request.query)
        unique_id = str(uuid.uuid4())
        return ChatResponse(msg=msg, id=unique_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    
@router.post("/chat_with_rag", response_model=ChatResponse)
def sync_chat(request: ChatRequest, background_tasks: BackgroundTasks):
    try:
        agent = AgentClass()
        msg = agent.generate_with_rag(request.query)
        unique_id = str(uuid.uuid4())
        return ChatResponse(msg=msg, id=unique_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.post("/env_stat", response_model=ChatResponse)
def sync_chat():
    try:
        agent = AgentClass()
        msg = agent.env_status()
        unique_id = str(uuid.uuid4())
        return ChatResponse(msg=msg, id=unique_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

