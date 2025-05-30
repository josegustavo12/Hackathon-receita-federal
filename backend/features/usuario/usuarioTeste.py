from usuario_service import UsuarioService
import json 

import os


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "usuarioBD.json")

with open(file_path, "r") as f:
        db = json.load(f)


#UsuarioService().criarUsuario(db, "jose", "123", "admin") -- deu certo
#print(UsuarioService().verificarSenha(db, "jose", "123")) -- deu certo