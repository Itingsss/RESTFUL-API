from fastapi import APIRouter, HTTPException, Query
from typing import List
from schemas.fakultas import (
    FKEkonomiBisnisInDB, 
    FKEkonomiBisnisCreate,
    FKEkonomiBisnisUpdate
)
from crud.fakultas import crud_fk_ekonomi

router = APIRouter(prefix="/fk_ekonomi", tags=["fakultas ekonomi"])

@router.get("/", response_model=List[FKEkonomiBisnisInDB])
async def get_all_ekonomi(
    skip: int = 0,
    limit: int = 100,
    gedung: str = None,
    lantai: int = None
):
    """Mendapatkan semua data fakultas ekonomi"""
    filters = {}
    if gedung:
        filters["gedung"] = gedung
    if lantai:
        filters["lantai"] = lantai
    
    data = crud_fk_ekonomi.get_multi(skip=skip, limit=limit, filters=filters)
    return data

@router.get("/{id}", response_model=FKEkonomiBisnisInDB)
async def get_ekonomi_by_id(id: int):
    """Mendapatkan data berdasarkan ID"""
    data = crud_fk_ekonomi.get(id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@router.get("/no/{no}", response_model=FKEkonomiBisnisInDB)
async def get_ekonomi_by_no(no: int):
    """Mendapatkan data berdasarkan nomor"""
    data = crud_fk_ekonomi.get_by_no(no)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@router.post("/", response_model=FKEkonomiBisnisInDB)
async def create_ekonomi(data_in: FKEkonomiBisnisCreate):
    """Membuat data baru"""
    # Cek duplikasi nomor
    existing = crud_fk_ekonomi.get_by_no(data_in.no)
    if existing:
        raise HTTPException(status_code=400, detail="Nomor already exists")
    
    data = crud_fk_ekonomi.create(data_in)
    return data

@router.put("/{id}", response_model=FKEkonomiBisnisInDB)
async def update_ekonomi(id: int, data_in: FKEkonomiBisnisUpdate):
    """Update data"""
    data = crud_fk_ekonomi.get(id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    
    # Cek jika no diupdate, pastikan tidak duplikat
    if data_in.no and data_in.no != data["no"]:
        existing = crud_fk_ekonomi.get_by_no(data_in.no)
        if existing:
            raise HTTPException(status_code=400, detail="Nomor already exists")
    
    updated_data = crud_fk_ekonomi.update(id, data_in)
    if not updated_data:
        raise HTTPException(status_code=400, detail="Update failed")
    
    return updated_data

@router.delete("/{id}")
async def delete_ekonomi(id: int):
    """Hapus data"""
    success = crud_fk_ekonomi.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail="Data not found")
    
    return {"message": "Data deleted successfully"}