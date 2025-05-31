import google.generativeai as genai
import re

class ProdutoIAService:
    def __init__(self):
        genai.configure(api_key="AIzaSyDo4b4jx421-CvM9m8uZNTKLgNKqss9f4g")
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def consultar_info_tecnica(self, marca: str, modelo: str) -> dict:
        prompt = (
            f"Liste separadamente e com títulos claros as seguintes informações técnicas do produto "
            f"da marca '{marca}', modelo '{modelo}': Bateria, Coil, Reservatório, Sensores, Circuito eletrônico, "
            f"e outros detalhes importantes. Escreva os títulos seguidos de dois-pontos."
        )
        response = self.model.generate_content(prompt).text.strip()

        campos = ["Bateria", "Coil", "Reservatório", "Sensores", "Circuito", "Outros"]
        info = {campo: "" for campo in campos}
        for campo in campos:
            match = re.search(f"{campo}: (.+?)(\n|$)", response, re.IGNORECASE)
            if match:
                info[campo] = match.group(1).strip()
        return info
