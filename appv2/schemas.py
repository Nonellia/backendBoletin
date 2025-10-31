from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
#Boletin
class BoletinBase(BaseModel):
    archivo: str
    categoria_id: int
    descripcion: str
    nombre: str
    observaciones: str
    fecha_creacion: date
    fecha_publicacion: date
    numero_string: str
    numero_int: int 
    accesible: bool

class BoletinCreate(BoletinBase):
    pass

class Boletin(BoletinBase):
    idboletin: int
    class Config:
        orm_mode = True

#Categoria
class CategoriaBase(BaseModel):
    nombre: str


class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    idcategoria: int
    class Config:
        orm_mode = True
#Usuarios
class UsuariosBase(BaseModel):
    nombre_completo: str
    ndni: int
    tipo_usuario: int
    usuario: str

class UsuariosCreate(UsuariosBase):
    password: str
    nombre_completo: str = Field(..., min_length=3, max_length=100)
    ndni: int = Field(..., ge=1000000, le=99999999)  # DNI válido
    tipo_usuario: int = Field(..., ge=0, le=2)  # Ejemplo: 0 = admin, 1 = usuario normal
    usuario: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)  # Contraseña mínima de 8 caracteres

class Usuarios(UsuariosBase):
    idusuarios: int

    class Config:
        orm_mode = True

# Para login
class UsuarioLogin(BaseModel):
    usuario: str
    password: str

# Respuesta de token
class Token(BaseModel):
    access_token: str
    token_type: str