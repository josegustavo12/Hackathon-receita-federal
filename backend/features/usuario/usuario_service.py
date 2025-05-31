import json
from fastapi import HTTPException
import hashlib
from backend.features.usuario.usuarioBD import UsuarioRequest
import os

USUARIO_DB = "features/usuario/usuarioBD.json"


class UsuarioService:
    def __init__(self):
        pass


    @staticmethod
    def hash_senha(senha: str) -> str:
        return hashlib.sha256(senha.encode()).hexdigest()

    @staticmethod
    def salvar_usuarios(db: dict):
        with open(USUARIO_DB, "w") as arquivo:
            json.dump(db, arquivo, indent=4)

    @staticmethod
    def criarUsuario(db: dict, request: UsuarioRequest):
        try:
            email = request.email
            senha = request.senha
            tipo = request.tipo

            if email in db:
                raise HTTPException(status_code=400, detail="Usuário já existe")

            hash_senha = UsuarioService.hash_senha(senha)

            db[email] = {
                "senha": hash_senha,
                "tipo": tipo
            }

            UsuarioService.salvar_usuarios(db)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao criar usuário: {str(e)}")

    @staticmethod
    def verificarSenha(db: dict, email: str, senha: str):
        usuario = db.get(email)

        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")

        hash_salvo = usuario.get("senha")
        hash_input = UsuarioService.hash_senha(senha)

        if hash_input != hash_salvo:
            raise HTTPException(status_code=401, detail="Senha incorreta")

        return {"mensagem": "Senha correta"}
        
    def deletarUsuario(email: str):
        if not os.path.exists(USUARIO_DB):
            raise HTTPException(status_code=500, detail="Arquivo de usuários não encontrado.")

        with open(USUARIO_DB, "r") as f:
            try:
                db = json.load(f)
            except json.JSONDecodeError:
                raise HTTPException(status_code=500, detail="Erro ao ler o banco de dados de usuários.")

        if email not in db:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")

        del db[email]

        with open(USUARIO_DB, "w") as f:
            json.dump(db, f, indent=4)

        return {"message": f"Usuário '{email}' deletado com sucesso."}
    

    def listarUsuarios():
        # Verifica se o arquivo existe
        if not os.path.exists(USUARIO_DB):
            return []

        try:
            with open(USUARIO_DB, "r") as f:
                data = json.load(f)
                return [
                    {"email": email, "tipo": info.get("tipo", "desconhecido")}
                    for email, info in data.items()
                ]
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="Erro ao ler banco de dados.")



