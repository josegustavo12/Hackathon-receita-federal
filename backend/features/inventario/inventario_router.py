from fastapi import APIRouter, HTTPException
from typing import List

from backend.features.inventario.inventarioBD import InventarioRequest
from backend.features.inventario.inventarioBD import InventarioInput
from backend.features.inventario.inventario_service import InventarioService as service
from backend.features.inventario.inventario_ia_services import ProdutoIAService

ia_service = ProdutoIAService()


router_public = APIRouter(
    prefix="/inventario",
    tags=["Inventário"]
)
router_private = APIRouter(
    prefix="/inventario",
    tags=["Inventário"]
)

@router_public.post("/analisar-ia/{item_id}", response_model=InventarioRequest)
def analisar_item_com_ia(item_id: str):
    item = service.buscar_por_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")

    info_ia = ia_service.consultar_info_tecnica(item.Marca, item.Modelo)

    atualizado = service.atualizar_campos_tecnicos(
        item_id=item.Id,
        info_ia=info_ia
    )

    if not atualizado:
        raise HTTPException(status_code=500, detail="Erro ao atualizar dados com IA")

    return atualizado

@router_public.get("/info-tecnica/{item_id}")
def obter_info_tecnica(item_id: str):
    item = service.buscar_por_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    
    resposta_ia = ia_service.consultar_info_tecnica(item.Marca, item.Modelo)
    return {"info_tecnica": resposta_ia}

@router_private.post("/", response_model=InventarioRequest) 
def criar_item(item: InventarioInput):
    novo_item = service.criar_item(
        item.Nome,
        item.Tipo,
        item.Marca,
        item.Modelo,
        item.Quantidade,
        item.Bateria,
        item.Coil,
        item.Reservatorio,
        item.Sensores,
        item.Circuito,
        item.Outros,
    )
    return novo_item

@router_public.get("/", response_model=List[InventarioRequest])
def listar_itens():
    return service.listar_itens()

@router_public.get("/{item_id}", response_model=InventarioRequest)
def buscar_item(item_id: str):
    item = service.buscar_por_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item

@router_private.put("/{item_id}", response_model=InventarioRequest)
def atualizar_item(item_id: str, item: InventarioRequest):
    atualizado = service.atualizar_item(
        item_id,
        item.Nome,
        item.Tipo,
        item.Marca,
        item.Modelo,
        item.Quantidade
    )
    if not atualizado:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return atualizado

@router_private.delete("/{item_id}")
def deletar_item(item_id: str):
    sucesso = service.deletar_item(item_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return {"ok": True}
