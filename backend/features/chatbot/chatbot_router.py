from fastapi import APIRouter
from chatbot_service import ChatbotService
from message import Message

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])

@router.post("/iniciar")
async def chat(msg : Message):
    obj = ChatbotService()
    return {"Resposta" : f"{obj.response(msg.message)}"}



