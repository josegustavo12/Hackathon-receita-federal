# Terceiros
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

# módulos
from backend.features.usuario.usuario_router import router_private as router_usuario_private
from backend.features.usuario.usuario_router import router_public as router_usuario_public
from backend.features.autenticacao.security import Security    
from backend.features.inventario.inventario_router import router_private as router_inventario_private
from backend.features.inventario.inventario_router import router_public as router_inventario_public
from backend.features.projetos.projetos_router import router_publica as router_projetos_public
from backend.features.projetos.projetos_router import router_privado as router_projetos_private
from backend.features.chatbot.chatbot_router import router as router_chatbot

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", 'http://172.16.23.41:8080/'], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# rota publica
public_routers = [router_usuario_public, router_inventario_public, router_chatbot, router_projetos_public]

for router in public_routers:
    app.include_router(router, prefix="/api")

# rota protegida ()
protected_routers = [router_inventario_private, router_projetos_private, router_usuario_private] 

for router in protected_routers:
    app.include_router(
        router,
        prefix="/api",
        dependencies=[Depends(Security.get_usuario_logado)]
    )
