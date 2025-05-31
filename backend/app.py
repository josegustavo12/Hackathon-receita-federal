# Terceiros
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

# módulos
from backend.features.usuario.usuario_router import router as usuario_router
from backend.features.autenticacao.security import Security     # função de dependência
from backend.features.inventario.inventario_router import router as inventario_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# rota publica
public_routers = []
app.include_router(usuario_router, prefix="/api")

# rota protegida ()
protected_routers = [inventario_router] 

for router in protected_routers:
    app.include_router(
        router,
        prefix="/api",
        dependencies=[Depends(Security.get_usuario_logado)]
    )
