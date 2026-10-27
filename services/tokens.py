from datetime import datetime, timedelta, timezone
import jwt
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("JWT_SECRET")
if not SECRET_KEY:
    raise RuntimeError("A variável JWT_SECRET não foi configurada.")
ALGORITHM = "HS256"


def criar_token(nome_usuario):
    expiracao = datetime.now(timezone.utc) + timedelta(minutes=30)
    payload = {
        "sub": nome_usuario,
        "exp": expiracao
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_token(token):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        usuario = payload.get("sub")
        if not usuario:
            return None
        return usuario
    except jwt.InvalidTokenError:
        return None