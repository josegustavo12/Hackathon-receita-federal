from fastapi import FastAPI
import uvicorn

from backend.features.inventario import inventarioBD
from backend.features.inventario import inventario_service
from backend.features.inventario import inventario_router

app = FastAPI(title="Inventário - Teste Local")

app.include_router(inventario_router.router_private)
app.include_router(inventario_router.router_public)



if __name__ == "__main__":
    uvicorn.run("features.inventario.main:app", host="127.0.0.1", port=8000, reload=True)
