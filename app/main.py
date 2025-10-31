from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal, engine, Base
from app.models import Base
from app.routers import boletin
from app.routers import categorias_documentos
from app.routers import expediente
from app.routers import documentos
from app.routers import anexos
from app.routers import articulos
from app.routers import personas_mentioned
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(boletin.router)
app.include_router(categorias_documentos.router)
app.include_router(expediente.router)
app.include_router(documentos.router)
app.include_router(anexos.router)
app.include_router(articulos.router)
app.include_router(personas_mentioned.router)
# Dependencia de la base de datos
def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
