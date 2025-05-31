from pydantic import BaseModel
from uuid import uuid4

class InventarioRequest(BaseModel):
    Id: str
    Nome: str
    Tipo: str
    Marca: str
    Modelo: str
    Quantidade: int
    Bateria: str = ""
    Coil: str = ""
    Reservatorio: str = ""
    Sensores: str = ""
    Circuito: str = ""
    Outros: str = ""

    @classmethod
    def criar_com_dados(cls, nome: str, tipo: str, marca: str, modelo: str, quantidade: int):
        return cls(
            Id=uuid4().hex,
            Nome=nome,
            Tipo=tipo,
            Marca=marca,
            Modelo=modelo,
            Quantidade=quantidade
        )
    
class InventarioInput(BaseModel):
    Nome: str
    Tipo: str
    Marca: str
    Modelo: str
    Quantidade: int