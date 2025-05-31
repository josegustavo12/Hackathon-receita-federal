import os
import json
from typing import List, Optional
from backend.features.inventario.inventarioBD import InventarioRequest


class InventarioService:
    DB_PATH = os.path.join(os.path.dirname(__file__), "inventarioBD.json")

    @classmethod
    def ler_banco(cls) -> List[InventarioRequest]:
        if not os.path.exists(cls.DB_PATH):
            with open(cls.DB_PATH, 'w') as f:
                json.dump([], f)

        with open(cls.DB_PATH, 'r') as f:
            data = json.load(f)
            return [InventarioRequest(**item) for item in data]

    @classmethod
    def salvar_banco(cls, dados: List[InventarioRequest]):
        with open(cls.DB_PATH, 'w') as f:
            json.dump([item.dict() for item in dados], f, indent=4)

    @classmethod
    def criar_item(cls, nome: str, tipo: str, quantidade: int) -> InventarioRequest:
        dados = cls.ler_banco()
        novo_item = InventarioRequest.criar_com_dados(nome, tipo, quantidade)
        dados.append(novo_item)
        cls.salvar_banco(dados)
        return novo_item

    @classmethod
    def listar_itens(cls) -> List[InventarioRequest]:
        return cls.ler_banco()

    @classmethod
    def buscar_por_id(cls, item_id: str) -> Optional[InventarioRequest]:
        return next((item for item in cls.ler_banco() if item.Id == item_id), None)

    @classmethod
    def atualizar_item(cls, item_id: str, nome: str, tipo: str, quantidade: int) -> Optional[InventarioRequest]:
        dados = cls.ler_banco()
        for i, item in enumerate(dados):
            if item.Id == item_id:
                dados[i] = InventarioRequest(Id=item_id, Nome=nome, Tipo=tipo, Quantidade=quantidade)
                cls.salvar_banco(dados)
                return dados[i]
        return None

    @classmethod
    def deletar_item(cls, item_id: str) -> bool:
        dados = cls.ler_banco()
        novos_dados = [item for item in dados if item.Id != item_id]
        if len(novos_dados) == len(dados):
            return False
        cls.salvar_banco(novos_dados)
        return True
