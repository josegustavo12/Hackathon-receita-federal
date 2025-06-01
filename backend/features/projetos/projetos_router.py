from fastapi import APIRouter, HTTPException
from typing import List
from .projetosBD import ProjetoRequest
from . import projetos_service as service

router_publica = APIRouter(
    prefix="/projetos",
    tags=["Projetos"]
)
router_privado = APIRouter(
    prefix="/projetos",
    tags=["Projetos"]
)

@router_privado.post("/", response_model=ProjetoRequest)
def criar_projeto(projeto: ProjetoRequest):
    novo = service.criar_projeto(
        projeto.Nome,
        projeto.Resumo,
        projeto.ComponentesNecessarios,
        projeto.NivelEscolaridade,
        projeto.Manual,
        projeto.Autor
    )
    return novo

@router_publica.get("/", response_model=List[ProjetoRequest])
def listar_projetos():
    return service.listar_projetos()

@router_publica.get("/{projeto_id}", response_model=ProjetoRequest)
def buscar_projeto(projeto_id: str):
    projeto = service.buscar_por_id(projeto_id)
    if not projeto:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return projeto

@router_privado.put("/{projeto_id}", response_model=ProjetoRequest)
def atualizar_projeto(projeto_id: str, projeto: ProjetoRequest):
    atualizado = service.atualizar_projeto(
        projeto_id,
        projeto.Nome,
        projeto.Resumo,
        projeto.ComponentesNecessarios,
        projeto.NivelEscolaridade,
        projeto.Manual,
        projeto.Autor
    )
    if not atualizado:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return atualizado

@router_privado.delete("/{projeto_id}")
def deletar_projeto(projeto_id: str):
    sucesso = service.deletar_projeto(projeto_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Projeto não encontrado")
    return {"mensagem": "Projeto deletado com sucesso"}
