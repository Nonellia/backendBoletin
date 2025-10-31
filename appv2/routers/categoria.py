from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud_base, schemas, database

router = APIRouter(prefix="/categoria", tags=["categoria"])

@router.post("/", response_model=schemas.Categoria)
def create_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(database.get_db)):
    return crud_base.categoria_crud.create(db, categoria)

@router.get("/", response_model=list[schemas.Categoria])
def read_categorias(db: Session = Depends(database.get_db)):
    return crud_base.categoria_crud.get_all(db)

@router.get("/{categoria_id}", response_model=schemas.Categoria)
def read_categoria(categoria_id: int, db: Session = Depends(database.get_db)):
    categoria = crud_base.categoria_crud.get(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria no encontrado")
    return categoria

@router.put("/{categoria_id}", response_model=schemas.Categoria)
def update_categoria(categoria_id: int, categoria: schemas.CategoriaCreate, db: Session = Depends(database.get_db)):
    db_obj = crud_base.categoria_crud.get(db, categoria_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Categoria no encontrado")
    updated = crud_base.categoria_crud.update(db, db_obj, categoria)
    return updated

@router.delete("/{categoria_id}")
def delete_categoria(categoria_id: int, db: Session = Depends(database.get_db)):
    db_obj = crud_base.categoria_crud.get(db, categoria_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Categoria no encontrado")
    crud_base.categoria_crud.delete(db, db_obj)
    return {"detail": "Categoria eliminado"}