from app.crud_base import CRUDBase
from app import models

class CRUDCategoria(CRUDBase):
    pass  # Podés agregar métodos específicos para Producto

categoria_crud = CRUDCategoria(models.Categoria)
