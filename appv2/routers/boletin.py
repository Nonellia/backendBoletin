from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from app import crud_base, schemas, database
import os
from datetime import date

router = APIRouter(prefix="/boletin", tags=["boletines"])

ITEMS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../items"))
os.makedirs(ITEMS_DIR, exist_ok=True)

@router.post("/", response_model=schemas.Boletin)
def create_boletin(boletin: schemas.BoletinCreate, db: Session = Depends(database.get_db)):
    return crud_base.boletin_crud.create(db, boletin)

@router.get("/", response_model=list[schemas.Boletin])
def read_boletins(db: Session = Depends(database.get_db)):
    return crud_base.boletin_crud.get_all(db)

@router.get("/{boletin_id}", response_model=schemas.Boletin)
def read_boletin(boletin_id: int, db: Session = Depends(database.get_db)):
    boletin = crud_base.boletin_crud.get(db, boletin_id)
    if not boletin:
        raise HTTPException(status_code=404, detail="Boletin no encontrado")
    return boletin

@router.put("/{boletin_id}", response_model=schemas.Boletin)
async def update_boletin(
    boletin_id: int,
    archivo: UploadFile = File(None),
    categoria_id: int = Form(...),
    descripcion: str = Form(...),
    nombre: str = Form(...),
    observaciones: str = Form(None),
    fecha_creacion: date = Form(...),
    fecha_publicacion: date = Form(...),
    numero_string: str = Form(None),
    numero_int: int = Form(None),
    accesible: int = Form(None),
    db: Session = Depends(database.get_db)
):
    db_obj = crud_base.boletin_crud.get(db, boletin_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Boletin no encontrado")
    archivo_nombre = db_obj.archivo
    if archivo is not None:
        # Guardar el archivo nuevo si se envía
        archivo_nombre = archivo.filename
        file_location = os.path.join(ITEMS_DIR, archivo.filename)
        with open(file_location, "wb") as f:
            f.write(await archivo.read())
    boletin_data = schemas.BoletinCreate(
        archivo=archivo_nombre,
        categoria_id=categoria_id,
        descripcion=descripcion,
        nombre=nombre,
        observaciones=observaciones,
        fecha_creacion=fecha_creacion,
        fecha_publicacion=fecha_publicacion,
        numero_string=numero_string,
        numero_int=numero_int,
        accesible=accesible
    )
    updated = crud_base.boletin_crud.update(db, db_obj, boletin_data)
    return updated

@router.delete("/{boletin_id}")
def delete_boletin(boletin_id: int, db: Session = Depends(database.get_db)):
    db_obj = crud_base.boletin_crud.get(db, boletin_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Boletin no encontrado")
    crud_base.boletin_crud.delete(db, db_obj)
    return {"detail": "Boletin eliminado"}

@router.post("/upload", response_model=schemas.Boletin)
async def upload_boletin(
    archivo: UploadFile = File(...),
    categoria_id: int = Form(...),
    descripcion: str = Form(...),
    nombre: str = Form(...),
    observaciones: str = Form(None),
    fecha_creacion: date = Form(...),
    fecha_publicacion: date = Form(...),
    numero_string: str = Form(None),
    numero_int: int = Form(None),
    accesible: int = Form(None),
    db: Session = Depends(database.get_db)
):
    # Guardar el archivo en la carpeta items
    file_location = os.path.join(ITEMS_DIR, archivo.filename)
    with open(file_location, "wb") as f:
        f.write(await archivo.read())

    boletin_data = schemas.BoletinCreate(
        archivo=archivo.filename,
        categoria_id=categoria_id,
        descripcion=descripcion,
        nombre=nombre,
        observaciones=observaciones,
        fecha_creacion=fecha_creacion,
        fecha_publicacion=fecha_publicacion,
        numero_string=numero_string,
        numero_int=numero_int,
        accesible=accesible
    )
    return crud_base.boletin_crud.create(db, boletin_data)