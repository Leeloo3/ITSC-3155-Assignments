from sqlalchemy.orm import Session
from fastapi import HTTPException, Response, status
from ..models import models, schemas

def create(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def read_all(db: Session):
    return db.query(models.Order).all()

def read_one(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def update(db: Session, order_id: int, order: schemas.OrderUpdate):
    db_order = db.query(models.Order).filter(models.Order.id == order_id)
    if not db_order.first():
        raise HTTPException(status_code=404, detail="Order not found")
    db_order.update(order.dict(exclude_unset=True))
    db.commit()
    return db_order.first()

def delete(db: Session, order_id: int):
    db_order = db.query(models.Order).filter(models.Order.id == order_id)
    if not db_order.first():
        raise HTTPException(status_code=404, detail="Order not found")
    db_order.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)