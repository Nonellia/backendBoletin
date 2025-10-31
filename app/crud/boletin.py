from app.crud_base import CRUDBase
from app import models

class CRUDBoletin(CRUDBase):
    pass  # Podés agregar métodos específicos para Producto

boletin_crud = CRUDBoletin(models.Boletin)