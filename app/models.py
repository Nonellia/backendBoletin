from sqlalchemy import Column, Integer, String, Text, Date, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import MetaData

# Convención de nombres para evitar conflictos con tablas de Laravel
metadata = MetaData()
Base = declarative_base(metadata=metadata)

class Documento(Base):
    __tablename__ = 'documentos'

    id = Column(Integer, primary_key=True)
    categoria_id = Column(Integer, ForeignKey('categorias_documento.id'))
    expediente_id = Column(Integer, ForeignKey('expedientes.id'))
    id_boletin = Column(Integer, ForeignKey('boletines.id'), nullable=False)
    numero_documento = Column(String(50), nullable=False)
    numero_completo = Column(String(100))
    fecha_emision = Column(Date, nullable=False)
    fecha_publicacion = Column(Date)
    lugar_emision = Column(String(100), default='RÍO GALLEGOS')
    contenido = Column(Text, nullable=False)
    estado = Column(String(50), default='BORRADOR')
    paginas = Column(String(50))
    anio_publicacion = Column(Integer)
    numero_edicion = Column(Integer)

    # Relaciones
    categoria = relationship("CategoriaDocumento", back_populates="documentos")
    expediente = relationship("Expediente", back_populates="documentos")
    boletin = relationship("Boletin", back_populates="documentos_rel")
    articulos = relationship("Articulo", back_populates="documento")
    anexos = relationship("Anexo", back_populates="documento")
    personas_mentioned = relationship("PersonaMencionada", back_populates="documento")


class CategoriaDocumento(Base):
    __tablename__ = 'categorias_documento'

    id = Column(Integer, primary_key=True)
    codigo = Column(String(10), unique=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    prefijo_numero = Column(String(20))
    plantilla = Column(Text)
    activo = Column(Boolean, default=True)

    documentos = relationship("Documento", back_populates="categoria")


class Expediente(Base):
    __tablename__ = 'expedientes'

    id = Column(Integer, primary_key=True)
    numero_expediente = Column(String(100), unique=True, nullable=False)
    organismo = Column(String(100))
    fecha_creacion = Column(Date)
    estado = Column(String(50), default='PENDIENTE')
    descripcion = Column(Text)

    documentos = relationship("Documento", back_populates="expediente")


class Boletin(Base):
    __tablename__ = 'boletines'

    id = Column(Integer, primary_key=True)
    numero_edicion = Column(Integer, nullable=False, unique=True)
    fecha_publicacion = Column(Date, nullable=False)
    anio_publicacion = Column(Integer)
    titulo_edicion = Column(String(200))
    documentos = Column(Text)   # Considerar cambiar a JSON en el futuro
    paginacion = Column(Text)   # Considerar cambiar a JSON en el futuro

    documentos_rel = relationship("Documento", back_populates="boletin")


class Articulo(Base):
    __tablename__ = 'articulos'

    id = Column(Integer, primary_key=True)
    documento_id = Column(Integer, ForeignKey('documentos.id'))
    numero_articulo = Column(String(10))
    tipo_articulo = Column(String(50))
    contenido = Column(Text, nullable=False)
    orden = Column(Integer, nullable=False, default=0)

    documento = relationship("Documento", back_populates="articulos")


class Anexo(Base):
    __tablename__ = 'anexos'

    id = Column(Integer, primary_key=True)
    documento_id = Column(Integer, ForeignKey('documentos.id'))
    tipo_anexo = Column(String(10))
    titulo = Column(String(200))
    contenido = Column(Text)
    es_tabla = Column(Boolean, default=False)

    documento = relationship("Documento", back_populates="anexos")


class PersonaMencionada(Base):
    __tablename__ = 'personas_mentioned'

    id = Column(Integer, primary_key=True)
    documento_id = Column(Integer, ForeignKey('documentos.id'))
    nombre_completo = Column(String(200))
    dni = Column(String(20))
    domicilio = Column(Text)
    tipo_mencion = Column(String(50))

    documento = relationship("Documento", back_populates="personas_mentioned")


# Tabla productos (opcional)
class Producto(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(String(255))
    precio = Column(Integer)
