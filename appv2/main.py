from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app import models, database
from app.routers import boletin
# from app.routers import categoria
from app.routers import usuarios
from app.routers import login, register

import os

# Crear tablas
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes poner aquí los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir archivos estáticos desde la carpeta items
items_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../items"))
app.mount("/items", StaticFiles(directory=items_dir), name="items")

# Incluir routers
# app.include_router(categoria.router)
app.include_router(boletin.router)
app.include_router(usuarios.router)
app.include_router(login.router)
app.include_router(register.router)