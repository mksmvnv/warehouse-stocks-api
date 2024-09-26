from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from db import models, schemas


def create_order(db: Session, order: schemas.OrderCreate) -> models.Order:
    db_order_items = []

    for item in order.items:
        # Check if product exists
        db_product = (
            db.query(models.Product)
            .filter(models.Product.id == item.product_id)
            .first()
        )

        if not db_product:
            raise HTTPException(
                status_code=404,
                detail=f"Product with id {item.product_id} not found",
            )

        if db_product.stock < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Not enough stock for product with id {item.product_id}",
            )

        # Update product stock
        db_product.stock -= item.quantity
        db_order_item = models.OrderItem(
            product_id=item.product_id, quantity=item.quantity
        )
        db_order_items.append(db_order_item)

    # Create order
    new_order = models.Order(order_items=db_order_item)

    try:
        db.add(new_order)
        db.commit()
        db.refresh(new_order)

        return new_order

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Database error during order creation: {e}"
        )


def get_order(db: Session, order_id: int) -> models.Order:
    # Check if order exists
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()

    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")

    return db_order


def get_orders(db: Session) -> list[models.Order]:
    # Check if orders exist
    db_orders = db.query(models.Order).all()

    if not db_orders:
        raise HTTPException(status_code=404, detail="Orders not found")

    return db_orders


def update_order_status(
    db: Session, order_id: int, status: models.OrderStatusEnum
) -> models.Order:
    # Check if order exists
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()

    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")

    # Update order status
    db_order.status = status

    try:
        db.commit()
        db.refresh(db_order)

        return db_order

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Database error during order update: {e}"
        )
