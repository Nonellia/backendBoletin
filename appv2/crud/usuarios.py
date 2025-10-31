from app.crud_base import CRUDBase
from app import models

class CRUDUsuarios(CRUDBase):
    pass  # Podés agregar métodos específicos para Producto

usuarios_crud = CRUDUsuarios(models.Usuarios)
