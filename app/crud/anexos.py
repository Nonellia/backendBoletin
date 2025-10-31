from app.crud_base import CRUDBase
from app import models

class CRUDAnexo(CRUDBase):
    pass 

anexo_crud = CRUDAnexo(models.Anexo)
