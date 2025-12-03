from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.database import db
from crud.user import crud_user

security = HTTPBearer()

def get_db() -> Generator:
    """Dependency untuk mendapatkan koneksi database"""
    with db.get_connection() as connection:
        yield connection

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """
    Dependency untuk mendapatkan user yang sedang login
    (Implementasi autentikasi akan ditambahkan kemudian)
    """
    # TODO: Implement JWT token validation
    token = credentials.credentials
    
    # Untuk sekarang, return user dummy
    # Nanti diganti dengan validasi JWT
    return {
        "id": 1,
        "username": "admin",
        "role": "admin"
    }

def get_current_admin(
    current_user: dict = Depends(get_current_user)
):
    """Dependency untuk memastikan user adalah admin"""
    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )
    return current_user

def pagination_params(
    skip: int = 0,
    limit: int = 100
):
    """Dependency untuk parameter pagination"""
    return {"skip": skip, "limit": limit}

def filter_params(
    gedung: str = None,
    lantai: int = None,
    fk: str = None,
    subUnit: str = None
):
    """Dependency untuk parameter filter"""
    filters = {}
    if gedung:
        filters["gedung"] = gedung
    if lantai:
        filters["lantai"] = lantai
    if fk:
        filters["fk"] = fk
    if subUnit:
        filters["subUnit"] = subUnit
    return filters