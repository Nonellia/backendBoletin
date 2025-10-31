from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud_base, schemas, database
from datetime import date

router = APIRouter(prefix="/personasmentioned", tags=["personasmentioned"])

@router.post("/", response_model=schemas.PersonaMencionada)
def create_expediente(expediente: schemas.PersonaMencionadaCreate, db: Session = Depends(database.get_db)):
    return crud_base.persona_mentioned_crud.create(db, expediente)

@router.get("/", response_model=list[schemas.PersonaMencionada])
def read_PersonaMencionada(db: Session = Depends(database.get_db)):
    return crud_base.persona_mentioned_crud.get_all(db)

@router.get("/{expediente_id}", response_model=schemas.PersonaMencionada)
def read_PersonaMencionada(PersonaMencionada_id: int, db: Session = Depends(database.get_db)):
    PersonaMencionada = crud_base.persona_mentioned_crud.get(db, PersonaMencionada_id)
    if not PersonaMencionada:
        raise HTTPException(status_code=404, detail="PersonaMencionada no encontrado")
    return PersonaMencionada

@router.put("/{expediente_id}", response_model=schemas.PersonaMencionada)
def update_PersonaMencionada(
    PersonaMencionada_id: int,
    PersonaMencionada: schemas.PersonaMencionadaCreate,
    db: Session = Depends(database.get_db)
):
    db_obj = crud_base.persona_mentioned_crud.get(db, PersonaMencionada_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="PersonaMencionada no encontrado")
    updated = crud_base.persona_mentioned_crud.update(db, db_obj, PersonaMencionada)
    return updated

@router.delete("/{expediente_id}")
def delete_PersonaMencionada(PersonaMencionada_id: int, db: Session = Depends(database.get_db)):
    db_obj = crud_base.persona_mentioned_crud.get(db, PersonaMencionada_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="PersonaMencionada no encontrado")
    crud_base.persona_mentioned_crud.delete(db, db_obj)
    return {"detail": "PersonaMencionada eliminado"}
