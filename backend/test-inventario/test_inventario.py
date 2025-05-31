import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from fastapi.testclient import TestClient
from features.inventario.main import app
from uuid import uuid4

client = TestClient(app)

def criar_item_valido(
    nome="Teclado",
    tipo="Periférico",
    marca="Logitech",
    modelo="K120",
    quantidade=5,
):
    return {
        "Nome": nome,
        "Tipo": tipo,
        "Marca": marca,
        "Modelo": modelo,
        "Quantidade": quantidade,
    }

def test_criar_item():
    item = criar_item_valido()
    response = client.post("/inventario/", json=item)
    assert response.status_code == 200
    data = response.json()
    assert data["Nome"] == item["Nome"]

def test_listar_itens():
    response = client.get("/inventario/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_buscar_por_id():
    item = criar_item_valido()
    post = client.post("/inventario/", json=item)
    assert post.status_code == 200

    result = post.json()
    item_id = result["Id"]  # ✅ pega o ID da resposta

    get = client.get(f"/inventario/{item_id}")
    assert get.status_code == 200

def test_editar_item():
    item = criar_item_valido()
    post = client.post("/inventario/", json=item)
    assert post.status_code == 200

    result = post.json()
    item_id = result["Id"]

    atualizado = item.copy()
    atualizado["Nome"] = "Teclado Mecânico"
    atualizado["Quantidade"] = 10
    atualizado["Marca"] = "Corsair"
    atualizado["Modelo"] = "K70"

    put = client.put(f"/inventario/{item_id}", json=atualizado)
    assert put.status_code == 422


def test_remover_item():
    item = criar_item_valido()
    post = client.post("/inventario/", json=item)
    assert post.status_code == 200

    result = post.json()
    item_id = result["Id"]

    delete = client.delete(f"/inventario/{item_id}")
    assert delete.status_code == 200


def test_atualizar_campos_ia():
    item = criar_item_valido()
    post = client.post("/inventario/", json=item)
    assert post.status_code == 200

    result = post.json()
    item_id = result["Id"]

    patch = client.patch(f"/inventario/{item_id}/atualizar_campos_ia")
    assert patch.status_code == 404

