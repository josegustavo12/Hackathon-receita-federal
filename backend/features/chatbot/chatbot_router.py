from fastapi import APIRouter
from backend.features.chatbot.chatbot_service import ChatbotService
from backend.features.chatbot.message import Message

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])

chat_sessions = {}


@router.post("/chat")
async def chat(msg: Message):
    user_id = msg.user_id  # precisa vir na requisição
    if user_id not in chat_sessions:
        chat_sessions[user_id] = ChatbotService()

    chatbot = chat_sessions[user_id]
    resposta = chatbot.response(msg.message)
    return {"Resposta": resposta}


