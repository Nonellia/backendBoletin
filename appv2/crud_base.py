from sqlalchemy.orm import Session
from app.models import Boletin
from app.models import Categoria
from app.models import Usuarios

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
        return db_obj

boletin_crud = CRUDBase(Boletin, "idboletin")
categoria_crud = CRUDBase(Categoria, "idcategoria")
usuarios_crud = CRUDBase(Usuarios, "idusuarios")