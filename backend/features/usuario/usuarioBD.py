from pydantic import BaseModel, EmailStr

class UsuarioRequest(BaseModel):
    CPF: str
    email: EmailStr
    senha: str 
    tipo: str