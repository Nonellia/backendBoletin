from app.crud_base import CRUDBase
from app import models

class CRUDExpediente(CRUDBase):
    pass  # Podés agregar métodos específicos para Producto

expediente_crud = CRUDExpediente(models.Expediente)