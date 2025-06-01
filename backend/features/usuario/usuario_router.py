from fastapi import APIRouter, HTTPException, status, Depends
from backend.features.usuario.usuarioBD import UsuarioRequest
from backend.features.usuario.usuario_service import UsuarioService
from backend.features.autenticacao.jwt import criar_token
from fastapi.security import OAuth2PasswordRequestForm
import json

DB_USUARIO = "features/usuario/usuarioBD.json"
router_private = APIRouter()
router_public = APIRouter()


@router_public.post("/usuario/login", tags=["Login"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        with open(DB_USUARIO, "r") as f:
            db = json.load(f)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao carregar o banco de dados: {str(e)}"
        )

    username = form_data.username
    senha = form_data.password

    usuario = db.get(username)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário inexistente"
        )

    hash_salvo = usuario.get("senha")
    if UsuarioService.hash_senha(senha) != hash_salvo:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Senha incorreta"
        )

    token = criar_token({"sub": username})
    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router_private.post("/usuario/newuser", tags=["Login"])
async def new_user(usuario: UsuarioRequest):
    try:
        with open(DB_USUARIO, "r") as f:
            db = json.load(f)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao carregar o banco de dados: {str(e)}"
        )

    try:
        UsuarioService.criarUsuario(db, usuario)
        return {"message": "Usuário criado com sucesso"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro interno ao criar usuário: {str(e)}"
        )

@router_private.delete("/usuario/{cpf}", tags=["Login"])
async def deletar_usuario(cpf: str):
    return UsuarioService.deletarUsuario(cpf)

@router_private.get("/usuario/listaruser", tags=["Login"])
async def Listar():
    return UsuarioService.listarUsuarios()
