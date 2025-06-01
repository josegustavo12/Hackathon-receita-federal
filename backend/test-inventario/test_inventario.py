import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import uuid
import random
import pytest
from fastapi.testclient import TestClient
from backend.features.inventario.main import app


client = TestClient(app)

def limpar_inventario():
    response = client.get("/inventario/")
    assert response.status_code == 200
    itens = response.json()
    for item in itens:
        client.delete(f"/inventario/{item['Id']}")

def gerar_pod():
    nomes = [
        "POD Vaze", "POD Juul", "POD Vinci", "POD Nord", "POD Caliburn",
        "POD Drag", "POD Elf Bar", "POD GeekVape", "POD Smok Novo",
        "POD Voopoo", "POD Renova", "POD Luxe", "POD Xros", "POD Aegis",
        "POD Orion", "POD Flexus", "POD Vinci Air", "POD Zero", "POD Mi-Pod", "POD Suorin"
    ]
    marcas = ["VapeTech", "Smok", "Voopoo", "Uwell", "GeekVape", "Vaporesso"]
    sensores = ["Fluxo de ar", "Temperatura", "Pressão", "Carga"]
    circuitos = ["Regulador de tensão", "Chip de proteção", "Microcontrolador", "PCB integrada"]

    nome = random.choice(nomes)
    return {
        "Id": str(uuid.uuid4().hex),
        "Nome": nome,
        "Tipo": "POD",
        "Marca": random.choice(marcas),
        "Modelo": f"Modelo {random.randint(100, 999)}",
        "Quantidade": random.randint(1, 20),
        "Bateria": "Litio recarregavel" if random.randint(1, 20) % 2 == 0 else "Lipo nao recarregavel",
        "Coil": "Coil Head" if random.randint(1, 20) > 10 else "Coil",
        "Reservatorio": f"{random.randint(1, 5)}ml",
        "Sensores": ", ".join(random.sample(sensores, k=random.randint(0, len(sensores)))) if random.randint(1, 20) > 12 else "",
        "Circuito": random.choice(circuitos) if random.randint(1, 20) > 15 else "",
        "Outros": "Cartucho substituivel" if random.randint(1, 20) > 15 else "",
    }

def test_reinserir_apenas_pods():
    limpar_inventario()

    for _ in range(100):
        pod = gerar_pod()
        response = client.post("/inventario/", json=pod)
        assert response.status_code == 200
        result = response.json()
        assert result["Nome"] == pod["Nome"]
        assert result["Tipo"] == "POD"
        assert result["Marca"] == pod["Marca"]
        assert result["Modelo"] == pod["Modelo"]
        assert result["Quantidade"] == pod["Quantidade"]
