import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI

from features.projetos import projetos_router

app = FastAPI()
app.include_router(projetos_router.router)
client = TestClient(app)

dados_teste = {
    "Id": "fake-id",
    "Nome": "Projeto Teste",
    "Resumo": "Um projeto de exemplo para testes",
    "ComponentesNecessarios": "Arduino, LEDs, Resistores",
    "NivelEscolaridade": "Ensino Médio",
    "Manual": "manual_teste.pdf",
    "Autor": "Mateus"
}

def test_criar_projeto():
    response = client.post("/projetos/", json=dados_teste)
    assert response.status_code == 200
    data = response.json()
    assert data["Nome"] == dados_teste["Nome"]
    global projeto_id
    projeto_id = data["Id"]  # salvar ID para os próximos testes

def test_listar_projetos():
    response = client.get("/projetos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_buscar_projeto_por_id():
    response = client.get(f"/projetos/{projeto_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["Id"] == projeto_id
    assert data["Nome"] == dados_teste["Nome"]

def test_atualizar_projeto():
    novos_dados = dados_teste.copy()
    novos_dados["Id"] = projeto_id
    novos_dados["Nome"] = "Projeto Atualizado"
    response = client.put(f"/projetos/{projeto_id}", json=novos_dados)
    assert response.status_code == 200
    assert response.json()["Nome"] == "Projeto Atualizado"

def test_deletar_projeto():
    response = client.delete(f"/projetos/{projeto_id}")
    assert response.status_code == 200
    assert "mensagem" in response.json()

def test_projeto_nao_encontrado():
    response = client.get("/projetos/nao-existe-id")
    assert response.status_code == 404
