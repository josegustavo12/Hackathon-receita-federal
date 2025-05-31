from pydantic import BaseModel
from uuid import uuid4

class InventarioRequest(BaseModel):
    Id: str
    Nome: str
    Tipo: str
    Quantidade: int

    @classmethod
    def criar_com_dados(cls, nome: str, tipo: str, quantidade: int):
        return cls(
            Id=uuid4().hex,
            Nome=nome,
            Tipo=tipo,
            Quantidade=quantidade
        )
