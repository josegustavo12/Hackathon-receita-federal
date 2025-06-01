import os
import json
from typing import List, Optional
from uuid import uuid4
from backend.features.inventario.inventarioBD import InventarioRequest
import datetime

class InventarioService:
    DB_PATH = os.path.join(os.path.dirname(__file__), "inventarioBD.json")


    @classmethod
    def ler_banco(cls) -> List[InventarioRequest]:
        # Se o arquivo não existe, cria com lista vazia
        if not os.path.exists(cls.DB_PATH):
            with open(cls.DB_PATH, 'w') as f:
                json.dump([], f)
        
        # Se o arquivo está vazio ou corrompido, sobrescreve com []
        try:
            with open(cls.DB_PATH, 'r') as f:
                content = f.read().strip()
                if not content:
                    data = []
                else:
                    data = json.loads(content)
        except (json.JSONDecodeError, FileNotFoundError):
            data = []
            with open(cls.DB_PATH, 'w') as f:
                json.dump(data, f)

        return [InventarioRequest(**item) for item in data]
    
    @classmethod
    def salvar_banco(cls, dados: List[InventarioRequest]):
        with open(cls.DB_PATH, 'w') as f:
            json.dump([item.dict() for item in dados], f, indent=4)

    @classmethod
    def criar_item(cls, nome: str, tipo: str, marca: str, modelo: str, quantidade: int) -> InventarioRequest:
        novo_item = InventarioRequest(
            Id=uuid4().hex,
            Nome=nome,
            Tipo=tipo,
            Marca=marca,
            Modelo=modelo,
            Quantidade=quantidade
        )
        dados = cls.ler_banco()
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
    def atualizar_item(cls, item_id: str, nome: str, tipo: str, marca: str, modelo: str, quantidade: int) -> Optional[InventarioRequest]:
        dados = cls.ler_banco()
        for i, item in enumerate(dados):
            if item.Id == item_id:
                dados[i] = InventarioRequest(
                    Id=item_id,
                    Nome=nome,
                    Tipo=tipo,
                    Marca=marca,
                    Modelo=modelo,
                    Quantidade=quantidade,
                    Bateria=item.Bateria,
                    Coil=item.Coil,
                    Reservatorio=item.Reservatorio,
                    Sensores=item.Sensores,
                    Circuito=item.Circuito,
                    Outros=item.Outros
                )
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

    @classmethod
    def atualizar_campos_tecnicos(cls, item_id: str, info_ia: dict) -> Optional[InventarioRequest]:
        dados = cls.ler_banco()
        for i, item in enumerate(dados):
            if item.Id == item_id:
                for campo, valor in info_ia.items():
                    if hasattr(item, campo):
                        setattr(item, campo, valor)
                cls.salvar_banco(dados)
                return item
        return None
