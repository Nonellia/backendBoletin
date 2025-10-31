from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud_base, schemas, database
from datetime import date

router = APIRouter(prefix="/expediente", tags=["expediente"])

@router.post("/", response_model=schemas.Expediente)
def create_expediente(expediente: schemas.ExpedienteCreate, db: Session = Depends(database.get_db)):
    return crud_base.expediente_crud.create(db, expediente)

@router.get("/", response_model=list[schemas.Expediente])
def read_Expediente(db: Session = Depends(database.get_db)):
    return crud_base.expediente_crud.get_all(db)

@router.get("/{expediente_id}", response_model=schemas.Expediente)
def read_Expediente(Expediente_id: int, db: Session = Depends(database.get_db)):
    Expediente = crud_base.expediente_crud.get(db, Expediente_id)
    if not Expediente:
        raise HTTPException(status_code=404, detail="Expediente no encontrado")
    return Expediente

@router.put("/{expediente_id}", response_model=schemas.Expediente)
def update_Expediente(
    Expediente_id: int,
    Expediente: schemas.ExpedienteCreate,
    db: Session = Depends(database.get_db)
):
    db_obj = crud_base.expediente_crud.get(db, Expediente_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Expediente no encontrado")
    updated = crud_base.expediente_crud.update(db, db_obj, Expediente)
    return updated

@router.delete("/{expediente_id}")
def delete_Expediente(Expediente_id: int, db: Session = Depends(database.get_db)):
    db_obj = crud_base.expediente_crud.get(db, Expediente_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Expediente no encontrado")
    crud_base.expediente_crud.delete(db, db_obj)
    return {"detail": "Expediente eliminado"}
