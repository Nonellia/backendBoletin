from app.crud_base import CRUDBase
from app import models

class CRUDDocumento(CRUDBase):
    pass  # Podés agregar métodos específicos para Producto

documento_crud = CRUDDocumento(models.Documentos, "id")