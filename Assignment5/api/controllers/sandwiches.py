from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models import models, schemas

def create(db: Session, sandwich: schemas.SandwichCreate):
    # Check if the sandwich name already exists
    existing_sandwich_by_name = db.query(models.Sandwich).filter(models.Sandwich.sandwich_name == sandwich.sandwich_name).first()
    if existing_sandwich_by_name:
        raise HTTPException(status_code=400, detail="Sandwich with this name already exists.")

    db_sandwich = models.Sandwich(**sandwich.model_dump())
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def read_all(db: Session):
    return db.query(models.Sandwich).all()

def read_one(db: Session, sandwich_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()

def update(db: Session, sandwich_id: int, sandwich: schemas.SandwichUpdate):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    if not db_sandwich.first():
        raise HTTPException(status_code=404, detail="Sandwich not found")
    db_sandwich.update(sandwich.dict(exclude_unset=True))
    db.commit()
    return db_sandwich.first()

def delete(db: Session, sandwich_id: int):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    if not db_sandwich.first():
        raise HTTPException(status_code=404, detail="Sandwich not found")
    db_sandwich.delete()
    db.commit() 



