from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas
from datetime import datetime


def create(db: Session, order: schemas.OrderCreate):
    # Create a new instance of the Order model with the provided data
    db_order = models.Order(
        customer_name=order.customer_name,
        description=order.description,
        order_date=datetime.now()  # Set the current date and time
    )
    # Add the newly created Order object to the database session
    db.add(db_order)
    # Commit the changes to the database
    db.commit()
    # Refresh the Order object to ensure it reflects the current state in the database
    db.refresh(db_order)

    # Create order details
    for detail in order.order_details:
        db_order_detail = models.OrderDetail(
            order_id=db_order.id,
            sandwich_id=detail.sandwich_id,
            amount=detail.amount
        )
        db.add(db_order_detail)

    db.commit()  # Commit the order details

    # Prepare the response structure
    order_response = schemas.Order(
        id=db_order.id,
        customer_name=db_order.customer_name,
        description=db_order.description,
        order_date=db_order.order_date,
        order_details=[
            schemas.OrderDetail(
                id=db_order_detail.id,
                amount=db_order_detail.amount,
                order_id=db_order_detail.order_id,
                sandwich=schemas.SandwichBase(
                    id=detail.sandwich_id,  # Assuming you have the sandwich ID
                    sandwich_name="Sample Sandwich",  # Replace with actual sandwich name if available
                    price=0  # Replace with actual price if available
                )
            )
            for db_order_detail in db_order.order_details
        ]
    )

    return order_response


def read_all(db: Session):
    return db.query(models.Order).all()


def read_one(db: Session, order_id):
    return db.query(models.Order).filter(models.Order.id == order_id).first()


def update(db: Session, order_id, order):
    # Query the database for the specific order to update
    db_order = db.query(models.Order).filter(models.Order.id == order_id)
    # Extract the update data from the provided 'order' object
    update_data = order.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_order.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated order record
    return db_order.first()


def delete(db: Session, order_id):
    # Query the database for the specific order to delete
    db_order = db.query(models.Order).filter(models.Order.id == order_id)
    # Delete the database record without synchronizing the session
    db_order.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
