from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud_base, schemas, database
from datetime import date

router = APIRouter(prefix="/anexo", tags=["anexo"])

@router.post("/", response_model=schemas.Anexo)
def create_Anexo(anexo: schemas.AnexoCreate, db: Session = Depends(database.get_db)):
    return crud_base.anexo_crud.create(db, anexo)

@router.get("/", response_model=list[schemas.Anexo])
def read_anexos(db: Session = Depends(database.get_db)):
    return crud_base.anexo_crud.get_all(db)

@router.get("/{anexo_id}", response_model=schemas.Anexo)
def read_anexo(anexo_id: int, db: Session = Depends(database.get_db)):
    anexo = crud_base.anexo_crud.get(db, anexo_id)
    if not anexo:
        raise HTTPException(status_code=404, detail="Anexo no encontrado")
    return anexo

@router.put("/{anexo_id}", response_model=schemas.Anexo)
def update_anexo(
    anexo_id: int,
    anexo: schemas.AnexoCreate,
    db: Session = Depends(database.get_db)
):
    db_obj = crud_base.anexo_crud.get(db, anexo_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Anexo no encontrado")
    updated = crud_base.anexo_crud.update(db, db_obj, anexo)
    return updated

@router.delete("/{anexo_id}")
def delete_anexo(anexo_id: int, db: Session = Depends(database.get_db)):
    db_obj = crud_base.anexo_crud.get(db, anexo_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Anexo no encontrado")
    crud_base.anexo_crud.delete(db, db_obj)
    return {"detail": "Anexo eliminado"}
