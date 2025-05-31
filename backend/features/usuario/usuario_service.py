import json
from fastapi import HTTPException
import hashlib
from pydantic import EmailStr, ValidationError


class UsuarioService:
    def __init__(self):
        pass

    @staticmethod
    def hash_senha(senha: str) -> str:
        return hashlib.sha256(senha.encode()).hexdigest()

    @staticmethod
    def salvar_usuarios(db: dict):
        with open("backend/features/usuario/usuarioBD.json", "w") as arquivo:
            json.dump(db, arquivo, indent=4)

    @staticmethod
    def criarUsuario(db: dict, request: dict):
        

        email = request["Email"]
        Senha = request["Senha"]
        Tipo = request["Tipo"]

        if email in db:
            raise HTTPException(status_code=400, detail="Usuário já existe")
        
        hashSenha = UsuarioService.hash_senha(Senha)

        try:

            db[email] = {"Senha" : hashSenha,
                         "Tipo" : Tipo}
            UsuarioService.salvar_usuarios(db)

        except Exception as e:
            return{
                "error" : str(e.json(indent=2)),
                "local" : "UsuarioService"
            }
    
    @staticmethod
    def verificarSenha(db: dict, Username: str, Senha: str):
        username = db.get(Username)
        hash_salvo = username["hashSenha"]
        if hash_salvo is None:
            raise HTTPException(
                status_code=404,
                detail="Usuário não encontrado"
            )
        
        hash_input = UsuarioService.hash_senha(Senha)
        if hash_input != hash_salvo:
            raise HTTPException(
                status_code=14,
                detail="Senha incorreta"
            )

        return {"mensagem": "Senha correta"}


            

