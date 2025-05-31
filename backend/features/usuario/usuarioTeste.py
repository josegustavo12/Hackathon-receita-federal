from usuario_service import UsuarioService
import json 

import os


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "usuarioBD.json")

with open(file_path, "r") as f:
        db = json.load(f)

testeUser = {
        "Email" : "josegustavovictor1@outlook.com",
        "Senha" : "123",
        "Tipo" : "admin"
}

UsuarioService().criarUsuario(db, testeUser)
#print(UsuarioService().verificarSenha(db, "jose", "123")) -- deu certo