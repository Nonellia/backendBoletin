from app.crud_base import CRUDBase
from app import models

class CRUDPersonaMentioned(CRUDBase):
    pass  # Podés agregar métodos específicos para Producto

persona_mentioned_crud = CRUDPersonaMentioned(models.PersonaMencionada)