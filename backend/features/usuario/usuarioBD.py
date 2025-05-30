from pydantic import BaseModel

class UsuarioRequest(BaseModel):
    Username: str
    Senha: str
    Tipo: str
