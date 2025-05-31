from pydantic import BaseModel, EmailStr

class UsuarioRequest(BaseModel):
    email: EmailStr
    senha: str 
    tipo: str