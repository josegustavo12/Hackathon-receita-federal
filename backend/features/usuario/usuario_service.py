import json
import hashlib
import os
import re
from pathlib import Path
from pydantic import EmailStr
from fastapi import HTTPException
from backend.features.usuario.usuarioBD import UsuarioRequest

USUARIO_DB = Path("features/usuario/usuarioBD.json")

class UsuarioService:
    def __init__(self):
        pass

    @staticmethod
    def hash_senha(senha: str) -> str:
        return hashlib.sha256(senha.encode()).hexdigest()

    @staticmethod
    def salvar_usuarios(db: dict) -> None:
        with open(USUARIO_DB, "w") as arquivo:
            json.dump(db, arquivo, indent=4)

    @staticmethod
    def validar_cpf(cpf: str) -> str:
        cpf = re.sub(r'\D', '', cpf)

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            raise ValueError("CPF inválido")

        def calcular_digito(cpf_parcial):
            soma = sum(int(digito) * peso for digito, peso in zip(cpf_parcial, range(len(cpf_parcial)+1, 1, -1)))
            resto = soma % 11
            return '0' if resto < 2 else str(11 - resto)

        digito1 = calcular_digito(cpf[:9])
        digito2 = calcular_digito(cpf[:9] + digito1)

        if cpf[-2:] != digito1 + digito2:
            raise ValueError("CPF inválido")

        return cpf

    @staticmethod
    def criarUsuario(db: dict, request: UsuarioRequest) -> None:
        try:
            cpf = UsuarioService.validar_cpf(request.CPF)
            email = request.email
            senha = request.senha
            tipo = "Comum"

            if email in db:
                raise HTTPException(status_code=400, detail="Usuário já existe")

            hash_senha = UsuarioService.hash_senha(senha)

            db[cpf] = {
                "senha": hash_senha,
                "tipo": tipo,
                "email": email
            }

            UsuarioService.salvar_usuarios(db)

        except ValueError as ve:
            raise HTTPException(status_code=400, detail=str(ve))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao criar usuário: {str(e)}")

    @staticmethod
    def verificarSenha(db: dict, email: str, senha: str) -> dict:
        usuario = db.get(email)

        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")

        hash_salvo = usuario.get("senha")
        hash_input = UsuarioService.hash_senha(senha)

        if hash_input != hash_salvo:
            raise HTTPException(status_code=401, detail="Senha incorreta")

        return {"mensagem": "Senha correta"}

    @staticmethod
    def deletarUsuario(email: str) -> dict:
        if not USUARIO_DB.exists():
            raise HTTPException(status_code=500, detail="Arquivo de usuários não encontrado.")

        try:
            with open(USUARIO_DB, "r") as f:
                db = json.load(f)
        except json.JSONDecodeError:
            raise HTTPException(status_code=500, detail="Erro ao ler o banco de dados.")

        if email not in db:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")

        del db[email]

        with open(USUARIO_DB, "w") as f:
            json.dump(db, f, indent=4)

        return {"message": f"Usuário '{email}' deletado com sucesso."}

    @staticmethod
    def listarUsuarios() -> list[dict]:
        if not USUARIO_DB.exists():
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
