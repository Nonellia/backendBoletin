from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud_base, schemas, database
from datetime import date

router = APIRouter(prefix="/documento", tags=["documento"])

@router.post("/", response_model=schemas.Documento)
def create_documento(documento: schemas.DocumentoCreate, db: Session = Depends(database.get_db)):
    return crud_base.documento_crud.create(db, documento)

@router.get("/", response_model=list[schemas.Documento])
def read_Documento(db: Session = Depends(database.get_db)):
    return crud_base.documento_crud.get_all(db)

@router.get("/{documento_id}", response_model=schemas.Documento)
def read_Documento(documento_id: int, db: Session = Depends(database.get_db)):
    Documento = crud_base.documento_crud.get(db, documento_id)
    if not Documento:
        raise HTTPException(status_code=404, detail="Documento no encontrado")
    return Documento

@router.put("/{documento_id}", response_model=schemas.Documento)
def update_Documento(
    Documento_id: int,
    Documento: schemas.DocumentoCreate,
    db: Session = Depends(database.get_db)
):
    db_obj = crud_base.documento_crud.get(db, Documento_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Documento no encontrado")
    updated = crud_base.documento_crud.update(db, db_obj, Documento)
    return updated

@router.delete("/{documento_id}")
def delete_Documento(Documento_id: int, db: Session = Depends(database.get_db)):
    db_obj = crud_base.documento_crud.get(db, Documento_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Documento no encontrado")
    crud_base.documento_crud.delete(db, db_obj)
    return {"detail": "Documento eliminado"}
