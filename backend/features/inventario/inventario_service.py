import os
import json
from typing import List, Optional
from features.inventario.inventarioBD import InventarioRequest

DB_PATH = os.path.join(os.path.dirname(__file__), "inventarioBD.json")

def ler_banco() -> List[InventarioRequest]:
    if not os.path.exists(DB_PATH):
        with open(DB_PATH, 'w') as f:
            json.dump([], f)
    with open(DB_PATH, 'r') as f:
        data = json.load(f)
        return [InventarioRequest(**item) for item in data]

def salvar_banco(dados: List[InventarioRequest]):
    with open(DB_PATH, 'w') as f:
        json.dump([item.dict() for item in dados], f, indent=4)

def criar_item(nome: str, tipo: str, quantidade: int) -> InventarioRequest:
    dados = ler_banco()
    novo_item = InventarioRequest.criar_com_dados(nome, tipo, quantidade)
    dados.append(novo_item)
    salvar_banco(dados)
    return novo_item

def listar_itens() -> List[InventarioRequest]:
    return ler_banco()

def buscar_por_id(item_id: str) -> Optional[InventarioRequest]:
    return next((item for item in ler_banco() if item.Id == item_id), None)

def atualizar_item(item_id: str, nome: str, tipo: str, quantidade: int) -> Optional[InventarioRequest]:
    dados = ler_banco()
    for i, item in enumerate(dados):
        if item.Id == item_id:
            dados[i] = InventarioRequest(Id=item_id, Nome=nome, Tipo=tipo, Quantidade=quantidade)
            salvar_banco(dados)
            return dados[i]
    return None

def deletar_item(item_id: str) -> bool:
    dados = ler_banco()
    novos_dados = [item for item in dados if item.Id != item_id]
    if len(novos_dados) == len(dados):
        return False
    salvar_banco(novos_dados)
    return True
