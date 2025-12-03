from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from schemas.user import UserInDB, UserCreate, UserUpdate
from crud.user import crud_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserInDB])
async def get_all_users(
    skip: int = 0,
    limit: int = 100
):
    """Mendapatkan semua user"""
    users = crud_user.get_multi(skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=UserInDB)
async def get_user(user_id: int):
    """Mendapatkan user berdasarkan ID"""
    user = crud_user.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserInDB)
async def create_user(user_in: UserCreate):
    """Membuat user baru"""
    existing_user = crud_user.get_by_username(user_in.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    user = crud_user.create(user_in)
    return user

@router.put("/{user_id}", response_model=UserInDB)
async def update_user(user_id: int, user_in: UserUpdate):
    """Update user"""
    user = crud_user.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    updated_user = crud_user.update(user_id, user_in)
    if not updated_user:
        raise HTTPException(status_code=400, detail="Update failed")
    
    return updated_user

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    """Hapus user"""
    success = crud_user.delete(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"message": "User deleted successfully"}