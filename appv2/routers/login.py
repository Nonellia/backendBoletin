from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, models, schemas
from app.auth import verify_password, create_access_token

router = APIRouter(prefix="/login", tags=["login"])

@router.post("/", response_model=schemas.Token)
def login(user: schemas.UsuarioLogin, db: Session = Depends(database.get_db)):
    db_user = db.query(models.Usuarios).filter(models.Usuarios.usuario == user.usuario).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    access_token = create_access_token(data={"sub": db_user.usuario})
    return {"access_token": access_token, "token_type": "bearer"}