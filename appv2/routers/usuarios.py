from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud_base, schemas, database

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.post("/", response_model=schemas.Usuarios)
def create_usuarios(usuarios: schemas.UsuariosCreate, db: Session = Depends(database.get_db)):
    return crud_base.usuarios_crud.create(db, usuarios)

@router.get("/", response_model=list[schemas.Usuarios])
def read_usuarioss(db: Session = Depends(database.get_db)):
    return crud_base.usuarios_crud.get_all(db)

@router.get("/{usuarios_id}", response_model=schemas.Usuarios)
def read_usuarios(usuarios_id: int, db: Session = Depends(database.get_db)):
    usuarios = crud_base.usuarios_crud.get(db, usuarios_id)
    if not usuarios:
        raise HTTPException(status_code=404, detail="Usuarios no encontrado")
    return usuarios

@router.put("/{usuarios_id}", response_model=schemas.Usuarios)
def update_usuarios(usuarios_id: int, usuarios: schemas.UsuariosCreate, db: Session = Depends(database.get_db)):
    db_obj = crud_base.usuarios_crud.get(db, usuarios_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Usuarios no encontrado")
    updated = crud_base.usuarios_crud.update(db, db_obj, usuarios)
    return updated

@router.delete("/{usuarios_id}")
def delete_usuarios(usuarios_id: int, db: Session = Depends(database.get_db)):
    db_obj = crud_base.usuarios_crud.get(db, usuarios_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Usuarios no encontrado")
    crud_base.usuarios_crud.delete(db, db_obj)
    return {"detail": "Usuarios eliminado"}