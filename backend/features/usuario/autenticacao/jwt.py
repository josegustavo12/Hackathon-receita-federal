from jose import jwt, JWTError
from datetime import datetime, timedelta

SECRET_KEY = "Iq=8PuPKskzvTFiXcmfpTKg#Au-iyX=6c6P7jetmYO#K+UZPQEa056BHK-yTkMzF"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 60 # aumentar para testar o frontend (1h é meio pouco eu acho)

def criar_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRATION_MINUTES) # tempo que irá expirar
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) # cria o token com o hs256

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None