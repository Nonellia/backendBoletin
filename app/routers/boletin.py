from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud_base, schemas, database
from datetime import date

router = APIRouter(prefix="/boletin", tags=["boletines"])

@router.post("/", response_model=schemas.Boletin)
def create_boletin(boletin: schemas.BoletinCreate, db: Session = Depends(database.get_db)):
    return crud_base.boletin_crud.create(db, boletin)

@router.get("/", response_model=list[schemas.Boletin])
def read_boletins(db: Session = Depends(database.get_db)):
    return crud_base.boletin_crud.get_all(db)

@router.get("/{boletin_id}", response_model=schemas.Boletin)
def read_boletin(boletin_id: int, db: Session = Depends(database.get_db)):
    boletin = crud_base.boletin_crud.get(db, boletin_id)
    if not boletin:
        raise HTTPException(status_code=404, detail="Boletin no encontrado")
    return boletin

@router.put("/{boletin_id}", response_model=schemas.Boletin)
def update_boletin(
    boletin_id: int,
    boletin: schemas.BoletinCreate,
    db: Session = Depends(database.get_db)
):
    db_obj = crud_base.boletin_crud.get(db, boletin_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Boletin no encontrado")
    updated = crud_base.boletin_crud.update(db, db_obj, boletin)
    return updated

@router.delete("/{boletin_id}")
def delete_boletin(boletin_id: int, db: Session = Depends(database.get_db)):
    db_obj = crud_base.boletin_crud.get(db, boletin_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Boletin no encontrado")
    crud_base.boletin_crud.delete(db, db_obj)
    return {"detail": "Boletin eliminado"}

@router.get("/{boletin_id}/full", response_model=schemas.BoletinWithDocuments)
def get_boletin_full(boletin_id: int, db: Session = Depends(database.get_db)):
    boletin = crud_base.boletin_crud.get(db, boletin_id)
    if not boletin:
        raise HTTPException(status_code=404, detail="Boletin no encontrado")
    documentos = db.query(crud_base.documento_crud.model).filter_by(id_boletin=boletin_id).all()
    documentos_rel = []
    for doc in documentos:
        articulos = db.query(crud_base.articulo_crud.model).filter_by(documento_id=doc.id).all()
        # print(f"Document ID: {doc.id}, Articulos encontrados: {len(articulos)}")
        anexos = db.query(crud_base.anexo_crud.model).filter_by(documento_id=doc.id).all()
        personas_mentioned = db.query(crud_base.persona_mentioned_crud.model).filter_by(documento_id=doc.id).all()
        categoria = None
        expediente = None
        if doc.categoria_id:
            categoria_obj = db.query(crud_base.categoria_documento_crud.model).get(doc.categoria_id)
            if categoria_obj:
                categoria = schemas.CategoriaDocumento.from_orm(categoria_obj)
        if doc.expediente_id:
            expediente_obj = db.query(crud_base.expediente_crud.model).get(doc.expediente_id)
            if expediente_obj:
                expediente = schemas.Expediente.from_orm(expediente_obj)
        doc_schema = schemas.DocumentoWithRelations.from_orm(doc)
        doc_schema.articulos = [schemas.Articulo.from_orm(a) for a in articulos]
        doc_schema.anexos = [schemas.Anexo.from_orm(a) for a in anexos]
        doc_schema.personas_mentioned = [schemas.PersonaMencionada.from_orm(p) for p in personas_mentioned]
        doc_schema.categoria = categoria
        doc_schema.expediente = expediente
        documentos_rel.append(doc_schema)
    boletin_schema = schemas.BoletinWithDocuments.from_orm(boletin)
    boletin_schema.documentos_rel = documentos_rel
    # for doc_schema in documentos_rel:
    #     print(doc_schema.articulos)
    return boletin_schema
