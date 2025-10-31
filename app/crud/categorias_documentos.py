from app.crud_base import CRUDBase
from app import models

class CRUDCategorias_Documento(CRUDBase):
    pass

cateogrias_documentos_crud = CRUDCategorias_Documento(models.CategoriaDocumento)