from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from app.models import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def authenticate_user(username: str, password: str):
    admin_username = "admin"
    admin_password = "admin"
    if username == admin_username and password == admin_password:
        # Gere um token de acesso
        token = jwt.encode({"username": username}, "secret", algorithm="HS256")
        return {"access_token": token}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

def verify_token(token: str):
    try:
        # Verifique o token e extraia o nome de usuário
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
        return payload["username"]
    except jwt.PyJWTError:
        return None