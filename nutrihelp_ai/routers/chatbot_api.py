# chatbot_api.py
from fastapi import APIRouter, HTTPException, UploadFile, File, WebSocket, WebSocketDisconnect, BackgroundTasks
from pydantic import BaseModel
from nutrihelp_ai.services.nutribot.Agents import AgentClass
from nutrihelp_ai.services.nutribot.AddDoc import AddDocClass

from openai import RateLimitError
import uuid
import asyncio

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
    
@router.post("/add_urls")
async def add_urls(urls: str):
    try:
        add_doc = AddDocClass()
        return await add_doc.add_urls(urls)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/add_pdfs")
async def add_pdfs(file: UploadFile = File(...)):
    try:
        add_doc = AddDocClass()
        return await add_doc.add_pdf(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    async def send_heartbeat():
        while True:
            try:
                await websocket.send_text("Ping")
                await asyncio.sleep(2)
            except Exception:
                break

    asyncio.create_task(send_heartbeat())
    try:
        while True:
            data = await websocket.receive_text()
            if data == "Pong":
                continue
            try:
                agent = AgentClass()
                async for chunk in agent.run_agent_ws(data):
                    await websocket.send_text(chunk)
                await websocket.send_text("##END##")
            except RateLimitError:
                await websocket.send_text("Rate Limit Error")
                break
            except Exception as e:
                await websocket.send_text(f"Error: {str(e)}")
                break
    except WebSocketDisconnect:
        pass
    finally:
        await websocket.close()


