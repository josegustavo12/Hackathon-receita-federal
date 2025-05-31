# Terceiros
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

# módulos
from backend.features.usuario.usuario_router import router_private as router_usuario_private
from backend.features.usuario.usuario_router import router_public as router_usuario_public
from backend.features.autenticacao.security import Security    
from backend.features.inventario.inventario_router import router_private as router_inventario_private
from backend.features.inventario.inventario_router import router_public as router_inventario_public
from backend.features.projetos.projetos_router import router as projetos_router
from backend.features.chatbot.chatbot_router import router as router_chatbot

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# rota publica
public_routers = [router_usuario_public, router_inventario_public, router_chatbot]

for router in public_routers:
    app.include_router(router, prefix="/api")

# rota protegida ()
protected_routers = [router_inventario_private, projetos_router, router_usuario_private] 

for router in protected_routers:
    app.include_router(
        router,
        prefix="/api",
        dependencies=[Depends(Security.get_usuario_logado)]
    )
