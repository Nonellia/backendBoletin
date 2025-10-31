from sqlalchemy.orm import Session
from app.models import Boletin
from app.models import CategoriaDocumento
from app.models import Expediente
from app.models import Documento
from app.models import Anexo
from app.models import PersonaMencionada
from app.models import Articulo
class CRUDBase:
    def __init__(self, model, id_field):
        self.model = model
        self.id_field = id_field

    def create(self, db: Session, obj_in):
        db_obj = self.model(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get(self, db: Session, obj_id: int):
        return db.query(self.model).filter(getattr(self.model, self.id_field) == obj_id).first()

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def update(self, db: Session, db_obj, obj_in):
        obj_data = obj_in.dict()
        for key, value in obj_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, db_obj):
        db.delete(db_obj)
        db.commit()

# Instancias CRUD para modelos principales (opcional, pero útil para import directo)
categoria_documento_crud = CRUDBase(CategoriaDocumento, "id")
anexo_crud = CRUDBase(Anexo, "id")
boletin_crud = CRUDBase(Boletin, "id")
expediente_crud = CRUDBase(Expediente, "id")
documento_crud = CRUDBase(Documento, "id")
persona_mentioned_crud = CRUDBase(PersonaMencionada, "id")
articulo_crud = CRUDBase(Articulo, "id")

