from pydantic import BaseModel
from uuid import uuid4

class ProjetoRequest(BaseModel):
    Id: str
    Nome: str
    Resumo: str
    ComponentesNecessarios: str
    NivelEscolaridade: str
    Manual: str
    Autor: str
    Data: str

    @classmethod
    def criar_com_dados(cls, nome: str, resumo: str, componentes: str, escolaridade: str, manual: str, autor: str, Data: str):
        return cls(
            Id=uuid4().hex,
            Nome=nome,
            Resumo=resumo,
            ComponentesNecessarios=componentes,
            NivelEscolaridade=escolaridade,
            Manual=manual,
            Autor=autor,
            Data=Data
        )
