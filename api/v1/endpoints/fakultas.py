from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from api.v1.dependencies import (
    get_current_user,
    get_current_admin,
    pagination_params,
    filter_params
)
from schemas.fakultas import (
    FakultasSyariahBase,
    FakultasDakwahBase,
    FakultasTarbiyahBase,
    FakultasHukumBase,
    FakultasPsikologiBase,
    FakultasMipaBase,
    FakultasTeknikBase,
    FakultasIKBase,
    FakultasKedokteranBase
)
from crud.fakultas import (
    crud_fk_syariah,
    crud_fk_dakwah,
    crud_fk_tarbiyah,
    crud_fk_hukum,
    crud_fk_psikologi,
    crud_fk_mipa,
    crud_fk_teknik,
    crud_fk_ik,
    crud_fk_kedokteran
)

router = APIRouter(prefix="/fakultas", tags=["fakultas"])

# Syariah
@router.get("/syariah", response_model=List[FakultasSyariahBase])
async def get_all_syariah(
    pagination: dict = Depends(pagination_params),
    filters: dict = Depends(filter_params),
    current_user: dict = Depends(get_current_user)
):
    """Mendapatkan semua data fakultas syariah"""
    return crud_fk_syariah.get_multi(**pagination, filters=filters)

@router.get("/syariah/{id}", response_model=FakultasSyariahBase)
async def get_syariah_by_id(
    id: int,
    current_user: dict = Depends(get_current_user)
):
    """Mendapatkan data syariah berdasarkan ID"""
    data = crud_fk_syariah.get(id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@router.post("/syariah", response_model=FakultasSyariahBase)
async def create_syariah(
    data_in: FakultasSyariahBase,
    current_user: dict = Depends(get_current_admin)
):
    """Membuat data syariah baru (admin only)"""
    existing = crud_fk_syariah.get_by_no(data_in.no)
    if existing:
        raise HTTPException(status_code=400, detail="Nomor already exists")
    return crud_fk_syariah.create(data_in)

@router.put("/syariah/{id}", response_model=FakultasSyariahBase)
async def update_syariah(
    id: int,
    data_in: dict,
    current_user: dict = Depends(get_current_admin)
):
    """Update data syariah (admin only)"""
    data = crud_fk_syariah.get(id)
    if not data:
        raise HTTPException(status_code=404, detail="Data not found")
    
    if data_in.get("no") and data_in["no"] != data["no"]:
        existing = crud_fk_syariah.get_by_no(data_in["no"])
        if existing:
            raise HTTPException(status_code=400, detail="Nomor already exists")
    
    return crud_fk_syariah.update(id, data_in)

@router.delete("/syariah/{id}")
async def delete_syariah(
    id: int,
    current_user: dict = Depends(get_current_admin)
):
    """Hapus data syariah (admin only)"""
    success = crud_fk_syariah.delete(id)
    if not success:
        raise HTTPException(status_code=404, detail="Data not found")
    return {"message": "Data deleted successfully"}

# Dakwah
@router.get("/dakwah", response_model=List[FakultasDakwahBase])
async def get_all_dakwah(
    pagination: dict = Depends(pagination_params),
    filters: dict = Depends(filter_params),
    current_user: dict = Depends(get_current_user)
):
    """Mendapatkan semua data fakultas dakwah"""
    return crud_fk_dakwah.get_multi(**pagination, filters=filters)

# Implementasi endpoint untuk dakwah sama seperti syariah
# ... (buat endpoint GET, POST, PUT, DELETE untuk dakwah)

# Tarbiyah
@router.get("/tarbiyah", response_model=List[FakultasTarbiyahBase])
async def get_all_tarbiyah(
    pagination: dict = Depends(pagination_params),
    filters: dict = Depends(filter_params),
    current_user: dict = Depends(get_current_user)
):
    """Mendapatkan semua data fakultas tarbiyah"""
    return crud_fk_tarbiyah.get_multi(**pagination, filters=filters)

# Hukum
@router.get("/hukum", response_model=List[FakultasHukumBase])
async def get_all_hukum(
    pagination: dict = Depends(pagination_params),
    filters: dict = Depends(filter_params),
    current_user: dict = Depends(get_current_user)
):
    """Mendapatkan semua data fakultas hukum"""
    return crud_fk_hukum.get_multi(**pagination, filters=filters)

# Psikologi
@router.get("/psikologi", response_model=List[FakultasPsikologiBase])
async def get_all_psikologi(
    pagination: dict = Depends(pagination_params),
    filters: dict = Depends(filter_params),
    current_user: dict = Depends(get_current_user)
):
    """Mendapatkan semua data fakultas psikologi"""
    return crud_fk_psikologi.get_multi(**pagination, filters=filters)

# MIPA
@router.get("/mipa", response_model=List[FakultasMipaBase])
async def get_all_mipa(
    pagination: dict = Depends(pagination_params),
    filters: dict = Depends(filter_params),
    current_user: dict = Depends(get_current_user)
):
    """Mendapatkan semua data fakultas MIPA"""
    return crud_fk_mipa.get_multi(**pagination, filters=filters)

# Teknik
@router.get("/teknik", response_model=List[FakultasTeknikBase])
async def get_all_teknik(
    pagination: dict = Depends(pagination_params),
    filters: dict = Depends(filter_params),
    current_user: dict = Depends(get_current_user)
):
    """Mendapatkan semua data fakultas teknik"""
    return crud_fk_teknik.get_multi(**pagination, filters=filters)

# Ilmu Komputer
@router.get("/ilmu-komputer", response_model=List[FakultasIKBase])
async def get_all_ilmu_komputer(
    pagination: dict = Depends(pagination_params),
    filters: dict = Depends(filter_params),
    current_user: dict = Depends(get_current_user)
):
    """Mendapatkan semua data fakultas ilmu komputer"""
    return crud_fk_ik.get_multi(**pagination, filters=filters)

# Kedokteran
@router.get("/kedokteran", response_model=List[FakultasKedokteranBase])
async def get_all_kedokteran(
    pagination: dict = Depends(pagination_params),
    filters: dict = Depends(filter_params),
    current_user: dict = Depends(get_current_user)
):
    """Mendapatkan semua data fakultas kedokteran"""
    return crud_fk_kedokteran.get_multi(**pagination, filters=filters)

# Search across all faculties
@router.get("/search")
async def search_all_faculties(
    query: str = Query(None, min_length=2, description="Search term"),
    gedung: str = None,
    lantai: int = None,
    current_user: dict = Depends(get_current_user)
):
    """Search data across all faculties"""
    # TODO: Implement search logic
    # This would require joining all tables or creating a view
    return {"message": "Search feature coming soon", "query": query}