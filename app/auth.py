import os
#const API_URL = "http://127.0.0.1:8000";
from datetime import datetime, timedelta, timezone

from jose import jwt, JWTError

from passlib.context import CryptContext

from fastapi import (
    Depends,
    HTTPException,
    status
)

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from .database import SessionLocal

from .models import User


SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "development-secret-key"
)

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


# ==========================================
# DATABASE
# ==========================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ==========================================
# PASSWORD
# ==========================================

def hash_password(
    password: str
):

    return pwd_context.hash(
        password
    )


def verify_password(
    password: str,
    password_hash: str
):

    return pwd_context.verify(
        password,
        password_hash
    )


# ==========================================
# JWT
# ==========================================

def create_access_token(
    user_id: int
):

    expire = (
        datetime.now(timezone.utc)
        +
        timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload = {
        "sub": str(user_id),
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


# ==========================================
# USUARIO AUTENTICADO
# ==========================================

def get_current_user(
    token: str = Depends(
        oauth2_scheme
    ),
    db: Session = Depends(get_db)
):

    credentials_error = HTTPException(
        status_code=401,
        detail="Token inválido o expirado",
        headers={
            "WWW-Authenticate": "Bearer"
        }
    )

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if not user_id:
            raise credentials_error

    except JWTError:

        raise credentials_error

    user = db.get(
        User,
        int(user_id)
    )

    if not user:
        raise credentials_error

    return user