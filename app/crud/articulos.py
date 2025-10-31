from app.crud_base import CRUDBase
from app import models

class CRUDArticulo(CRUDBase):
    pass  # Podés agregar métodos específicos para Producto

articulo_crud = CRUDArticulo(models.Articulo)