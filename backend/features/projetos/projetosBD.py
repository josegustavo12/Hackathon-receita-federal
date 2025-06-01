from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import date

class ProjetoRequest(BaseModel):
    Id: str = Field(default_factory=lambda: uuid4().hex)
    Nome: str
    Resumo: str
    ComponentesNecessarios: str
    NivelEscolaridade: str
    Manual: str
    Autor: str
    Data: str = Field(default_factory=lambda: date.today().isoformat())

    @classmethod
    def criar_com_dados(cls, nome: str, resumo: str, componentes: str, escolaridade: str, manual: str, autor: str):
        return cls(
            Nome=nome,
            Resumo=resumo,
            ComponentesNecessarios=componentes,
            NivelEscolaridade=escolaridade,
            Manual=manual,
            Autor=autor
        )
