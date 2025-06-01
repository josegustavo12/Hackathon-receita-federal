import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

class ChatbotService:
    def __init__(self, max_length=2000):
        genai.configure(api_key="API_KEY_GEMINI")
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Prompt inicial para guiar o comportamento da IA
        self.system_prompt = (
            "Gemini, as perguntas prévias do usuário estão depois de 'Usuário: '"
            " e suas respostas previas estão depois de 'Assistente', porém quando"
            " você for responder não digite 'Assistente' no início."
        )
        
        # Conversa começa com o system prompt e usuário
        self.conversation = f"{self.system_prompt}\nUsuário: "
        self.max_length = max_length

    def response(self, text):
        self.conversation += text
        if len(self.conversation) > self.max_length:
            self.trim_conversation()
        response = self.model.generate_content(self.conversation)
        self.conversation += f"\nAssistente: {response.text}\nUsuário: "
        return response.text

    def trim_conversation(self):
        trimmed = self.conversation[-self.max_length:]
        idx = trimmed.find("\nUsuário: ")
        if idx != -1:
            self.conversation = trimmed[idx + 1:]
        else:
            self.conversation = trimmed

    def restart(self):
        self.conversation = f"{self.system_prompt}\nUsuário: "


