from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Boletin(Base):
    __tablename__ = "boletin"
    idboletin = Column(Integer, primary_key=True, index=True)
    archivo = Column(String)
    categoria_id = Column(Integer)
    descripcion = Column(String(255))
    nombre = Column(String(255))
    observaciones = Column(String(45))
    fecha_creacion = Column(Date)
    fecha_publicacion = Column(Date)
    numero_string = Column(String(255))
    numero_int = Column(Integer)
    accesible = Column(Integer)  
class Categoria(Base):
    __tablename__ = "categoria"
    idcategoria = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
class Usuarios(Base):
    __tablename__ = "usuarios"

    idusuarios = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String, nullable=False)
    ndni = Column(Integer, nullable=False, default=0)
    tipo_usuario = Column(Integer, nullable=False, default=0)
    usuario = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)