from pydantic import BaseModel, EmailStr

class UsuarioRequest(BaseModel):
    email: EmailStr
    Senha: str
    Tipo: str # admin, user-escolar, user-receita, user-projetos
    

