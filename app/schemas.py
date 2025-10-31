from pydantic import BaseModel
from datetime import date
from typing import Optional, List

# Schemas base
class CategoriaDocumentoBase(BaseModel):
    codigo: str
    nombre: str
    prefijo_numero: Optional[str] = None
    plantilla: Optional[str] = None
    activo: bool = True

class CategoriaDocumentoCreate(CategoriaDocumentoBase):
    pass

class CategoriaDocumento(CategoriaDocumentoBase):
    id: int
    
    class Config:
        from_attributes = True

class ExpedienteBase(BaseModel):
    numero_expediente: str
    organismo: Optional[str] = None
    fecha_creacion: Optional[date] = None
    estado: str = 'PENDIENTE'
    descripcion: Optional[str] = None

class ExpedienteCreate(ExpedienteBase):
    pass

class Expediente(ExpedienteBase):
    id: int
    
    class Config:
        from_attributes = True

class BoletinBase(BaseModel):
    numero_edicion: int
    fecha_publicacion: date
    anio_publicacion: Optional[int] = None
    titulo_edicion: Optional[str] = None
    documentos: Optional[str] = None
    paginacion: Optional[str] = None

class BoletinCreate(BoletinBase):
    pass

class Boletin(BoletinBase):
    id: int
    
    class Config:
        from_attributes = True

class DocumentoBase(BaseModel):
    categoria_id: Optional[int] = None
    expediente_id: Optional[int] = None
    id_boletin: int
    numero_documento: str
    numero_completo: Optional[str] = None
    fecha_emision: date
    fecha_publicacion: Optional[date] = None
    lugar_emision: str = 'RÍO GALLEGOS'
    contenido: str
    estado: str = 'BORRADOR'
    paginas: Optional[str] = None
    anio_publicacion: Optional[int] = None
    numero_edicion: Optional[int] = None

class DocumentoCreate(DocumentoBase):
    pass

class Documento(DocumentoBase):
    id: int
    categoria: Optional[CategoriaDocumento] = None
    expediente: Optional[Expediente] = None
    boletin: Optional[Boletin] = None
    
    class Config:
        from_attributes = True

class ArticuloBase(BaseModel):
    documento_id: Optional[int] = None
    numero_articulo: Optional[str] = None
    tipo_articulo: Optional[str] = None
    contenido: str
    orden: int = 0

class ArticuloCreate(ArticuloBase):
    pass

class Articulo(ArticuloBase):
    id: int
    
    class Config:
        from_attributes = True

class AnexoBase(BaseModel):
    documento_id: Optional[int] = None
    tipo_anexo: Optional[str] = None
    titulo: Optional[str] = None
    contenido: Optional[str] = None
    es_tabla: bool = False

class AnexoCreate(AnexoBase):
    pass

class Anexo(AnexoBase):
    id: int
    
    class Config:
        from_attributes = True

class PersonaMencionadaBase(BaseModel):
    documento_id: Optional[int] = None
    nombre_completo: Optional[str] = None
    dni: Optional[str] = None
    domicilio: Optional[str] = None
    tipo_mencion: Optional[str] = None

class PersonaMencionadaCreate(PersonaMencionadaBase):
    pass

class PersonaMencionada(PersonaMencionadaBase):
    id: int
    
    class Config:
        from_attributes = True

class ProductoBase(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[int] = None

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int
    
    class Config:
        from_attributes = True

# Schemas con relaciones
class DocumentoWithRelations(Documento):
    articulos: List[Articulo] = []
    anexos: List[Anexo] = []
    personas_mentioned: List[PersonaMencionada] = []
    categoria: Optional[CategoriaDocumento] = None
    expediente: Optional[Expediente] = None

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

class BoletinWithDocuments(Boletin):
    documentos_rel: List[DocumentoWithRelations] = []

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True