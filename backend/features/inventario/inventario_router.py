from fastapi import APIRouter, HTTPException
from typing import List

from .inventarioBD import InventarioRequest
from . import inventario_service as service

router = APIRouter(
    prefix="/inventario",
    tags=["Inventário"]
)

@router.post("/", response_model=InventarioRequest)
def criar_item(item: InventarioRequest):
    novo_item = service.criar_item(item.Nome, item.Tipo, item.Quantidade)
    return novo_item

@router.get("/", response_model=List[InventarioRequest])
def listar_itens():
    return service.listar_itens()

@router.get("/{item_id}", response_model=InventarioRequest)
def buscar_item(item_id: str):
    item = service.buscar_por_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item

@router.put("/{item_id}", response_model=InventarioRequest)
def atualizar_item(item_id: str, item: InventarioRequest):
    atualizado = service.atualizar_item(item_id, item.Nome, item.Tipo, item.Quantidade)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return atualizado

@router.delete("/{item_id}")
def deletar_item(item_id: str):
    sucesso = service.deletar_item(item_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return {"mensagem": "Item deletado com sucesso"}
