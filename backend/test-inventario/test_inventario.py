import pytest
from fastapi.testclient import TestClient
from features.inventario.main import app
from uuid import uuid4

client = TestClient(app)

def criar_item_valido(nome="Teclado", tipo="Periférico", quantidade=5):
    return {
        "Id": uuid4().hex,
        "Nome": nome,
        "Tipo": tipo,
        "Quantidade": quantidade
    }

def test_criar_item():
    item = criar_item_valido()
    response = client.post("/inventario/", json=item)
    assert response.status_code == 200
    data = response.json()
    assert data["Nome"] == item["Nome"]
    assert data["Tipo"] == item["Tipo"]
    assert data["Quantidade"] == item["Quantidade"]

def test_listar_itens():
    response = client.get("/inventario/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_buscar_por_id():
    item = criar_item_valido()
    post = client.post("/inventario/", json=item)
    assert post.status_code == 200
    item_id = item["Id"]

    get = client.get(f"/inventario/{item_id}")
    assert get.status_code == 200
    assert get.json()["Id"] == item_id

def test_editar_item():
    item = criar_item_valido()
    post = client.post("/inventario/", json=item)
    assert post.status_code == 200

    atualizado = item.copy()
    atualizado["Nome"] = "Teclado Mecânico"
    atualizado["Quantidade"] = 10

    put = client.put(f"/inventario/{item['Id']}", json=atualizado)
    assert put.status_code == 200
    assert put.json()["Nome"] == "Teclado Mecânico"
    assert put.json()["Quantidade"] == 10

def test_remover_item():
    item = criar_item_valido()
    post = client.post("/inventario/", json=item)
    assert post.status_code == 200

    delete = client.delete(f"/inventario/{item['Id']}")
    assert delete.status_code == 200
    assert delete.json()["ok"] is True

    get = client.get(f"/inventario/{item['Id']}")
    assert get.status_code == 404
