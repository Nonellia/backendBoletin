from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud_base, schemas, database
from datetime import date

router = APIRouter(prefix="/categoriadocumento", tags=["categoriadocumento"])

@router.post("/", response_model=schemas.CategoriaDocumento)
def create_categoriadocumento(categoriadocumento: schemas.CategoriaDocumentoCreate, db: Session = Depends(database.get_db)):
    return crud_base.categoria_documento_crud.create(db, categoriadocumento)

@router.get("/", response_model=list[schemas.CategoriaDocumento])
def read_categoriadocumentos(db: Session = Depends(database.get_db)):
    return crud_base.categoria_documento_crud.get_all(db)

@router.get("/{categoriadocumento_id}", response_model=schemas.CategoriaDocumento)
def read_categoriadocumento(categoriadocumento_id: int, db: Session = Depends(database.get_db)):
    categoriadocumento = crud_base.categoria_documento_crud.get(db, categoriadocumento_id)
    if not categoriadocumento:
        raise HTTPException(status_code=404, detail="CategoriaDocumento no encontrado")
    return categoriadocumento

@router.put("/{categoriadocumento_id}", response_model=schemas.CategoriaDocumento)
def update_categoriadocumento(
    categoriadocumento_id: int,
    categoriadocumento: schemas.CategoriaDocumentoCreate,
    db: Session = Depends(database.get_db)
):
    db_obj = crud_base.categoria_documento_crud.get(db, categoriadocumento_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="CategoriaDocumento no encontrado")
    updated = crud_base.categoria_documento_crud.update(db, db_obj, categoriadocumento)
    return updated

@router.delete("/{categoriadocumento_id}")
def delete_categoriadocumento(categoriadocumento_id: int, db: Session = Depends(database.get_db)):
    db_obj = crud_base.categoria_documento_crud.get(db, categoriadocumento_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="CategoriaDocumento no encontrado")
    crud_base.categoria_documento_crud.delete(db, db_obj)
    return {"detail": "CategoriaDocumento eliminado"}
