import os
import json
from typing import List, Optional
from .projetosBD import ProjetoRequest

DB_PATH = os.path.join(os.path.dirname(__file__), "projetosBD.json")

def ler_banco() -> List[ProjetoRequest]:
    if not os.path.exists(DB_PATH):
        with open(DB_PATH, 'w') as f:
            json.dump([], f)

    if os.path.getsize(DB_PATH) == 0:
        with open(DB_PATH, 'w') as f:
            json.dump([], f)

    with open(DB_PATH, 'r') as f:
        data = json.load(f)
        return [ProjetoRequest(**item) for item in data]

def salvar_banco(dados: List[ProjetoRequest]):
    with open(DB_PATH, 'w') as f:
        json.dump([item.dict() for item in dados], f, indent=4)

def criar_projeto(nome: str, resumo: str, componentes: str, escolaridade: str, manual: str, autor: str) -> ProjetoRequest:
    dados = ler_banco()
    novo = ProjetoRequest.criar_com_dados(nome, resumo, componentes, escolaridade, manual, autor)
    dados.append(novo)
    salvar_banco(dados)
    return novo

def listar_projetos() -> List[ProjetoRequest]:
    return ler_banco()

def buscar_por_id(projeto_id: str) -> Optional[ProjetoRequest]:
    return next((p for p in ler_banco() if p.Id == projeto_id), None)

def atualizar_projeto(projeto_id: str, nome: str, resumo: str, componentes: str, escolaridade: str, manual: str, autor: str) -> Optional[ProjetoRequest]:
    dados = ler_banco()
    for i, projeto in enumerate(dados):
        if projeto.Id == projeto_id:
            dados[i] = ProjetoRequest(
                Id=projeto_id,
                Nome=nome,
                Resumo=resumo,
                ComponentesNecessarios=componentes,
                NivelEscolaridade=escolaridade,
                Manual=manual,
                Autor=autor
            )
            salvar_banco(dados)
            return dados[i]
    return None

def deletar_projeto(projeto_id: str) -> bool:
    dados = ler_banco()
    novos_dados = [p for p in dados if p.Id != projeto_id]
    if len(novos_dados) == len(dados):
        return False
    salvar_banco(novos_dados)
    return True
