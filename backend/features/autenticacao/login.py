from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from backend.features.autenticacao.jwt import verificar_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/usuario/login")

def get_usuario_logado(token: str = Depends(oauth2_scheme)):
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload 
