from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, models, schemas
from app.auth import get_password_hash

router = APIRouter(prefix="/register", tags=["register"])

@router.post("/", response_model=schemas.Usuarios)
def register(user: schemas.UsuariosCreate, db: Session = Depends(database.get_db)):
    # Verificar si el usuario ya existe
    db_user = db.query(models.Usuarios).filter(models.Usuarios.usuario == user.usuario).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    # Hashear la contraseña
    hashed_password = get_password_hash(user.password)
    
    # Crear nuevo usuario
    new_user = models.Usuarios(
        nombre_completo=user.nombre_completo,
        ndni=user.ndni,
        tipo_usuario=user.tipo_usuario,
        usuario=user.usuario,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user