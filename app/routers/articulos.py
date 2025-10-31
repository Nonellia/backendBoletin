from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud_base, schemas, database
from datetime import date

router = APIRouter(prefix="/articulo", tags=["articulo"])

@router.post("/", response_model=schemas.Articulo)
def create_Articulo(articulo: schemas.ArticuloCreate, db: Session = Depends(database.get_db)):
    return crud_base.articulo_crud.create(db, articulo)

@router.get("/", response_model=list[schemas.Articulo])
def read_articulos(db: Session = Depends(database.get_db)):
    return crud_base.articulo_crud.get_all(db)

@router.get("/{articulo_id}", response_model=schemas.Articulo)
def read_articulo(articulo_id: int, db: Session = Depends(database.get_db)):
    articulo = crud_base.articulo_crud.get(db, articulo_id)
    if not articulo:
        raise HTTPException(status_code=404, detail="Articulo no encontrado")
    return articulo

@router.put("/{articulo_id}", response_model=schemas.Articulo)
def update_articulo(
    articulo_id: int,
    articulo: schemas.ArticuloCreate,
    db: Session = Depends(database.get_db)
):
    db_obj = crud_base.articulo_crud.get(db, articulo_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Articulo no encontrado")
    updated = crud_base.articulo_crud.update(db, db_obj, articulo)
    return updated

@router.delete("/{articulo_id}")
def delete_articulo(articulo_id: int, db: Session = Depends(database.get_db)):
    db_obj = crud_base.articulo_crud.get(db, articulo_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Articulo no encontrado")
    crud_base.articulo_crud.delete(db, db_obj)
    return {"detail": "Articulo eliminado"}
