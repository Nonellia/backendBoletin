from typing import Optional
from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from app.crud_base import boletin_crud
from app.database import get_db

router = APIRouter()

@router.put("/boletin/{idboletin}")
async def update_boletin(
    idboletin: int,
    archivo: Optional[UploadFile] = File(None),
    categoria_id: Optional[int] = Form(None),
    descripcion: Optional[str] = Form(None),
    nombre: Optional[str] = Form(None),
    observaciones: Optional[str] = Form(None),
    fecha_creacion: Optional[str] = Form(None),
    fecha_publicacion: Optional[str] = Form(None),
    numero_string: Optional[str] = Form(None),
    numero_int: Optional[int] = Form(None),
    accesible: Optional[int] = Form(None),
    db: Session = Depends(get_db)
):
    db_obj = boletin_crud.get(db, idboletin)
    if not db_obj:
        return {"error": "Boletín no encontrado"}
    # Si hay archivo nuevo, procesalo y guarda el nombre/ruta
    if archivo:
        db_obj.archivo = archivo.filename
        # ...guardar archivo en disco...
    # Actualizar el resto de los campos solo si vienen
    if categoria_id is not None: db_obj.categoria_id = categoria_id
    if descripcion is not None: db_obj.descripcion = descripcion
    if nombre is not None: db_obj.nombre = nombre
    if observaciones is not None: db_obj.observaciones = observaciones
    if fecha_creacion is not None: db_obj.fecha_creacion = fecha_creacion
    if fecha_publicacion is not None: db_obj.fecha_publicacion = fecha_publicacion
    if numero_string is not None: db_obj.numero_string = numero_string
    if numero_int is not None: db_obj.numero_int = numero_int
    if accesible is not None: db_obj.accesible = accesible
    db.commit()
    db.refresh(db_obj)
    return db_obj