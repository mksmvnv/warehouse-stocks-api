from fastapi import HTTPException

from sqlalchemy.orm import Session

from db import models, schemas


def create_order(db: Session, order: schemas.OrderCreate) -> models.Order:
    order_items = []

    try:
        for item in order.items:
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

            db_product.stock -= item.quantity
            db_order_item = models.OrderItem(
                product_id=item.product_id, quantity=item.quantity
            )
            order_items.append(db_order_item)

        db_order = models.Order(order_items=order_items)
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order

    except:
        db.rollback()
        raise


def get_order(db: Session, order_id: int) -> models.Order:
    order = db.query(models.Order).filter(models.Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order


def get_orders(db: Session) -> list[models.Order]:
    orders = db.query(models.Order).all()

    if not orders:
        raise HTTPException(status_code=404, detail="Orders not found")

    return orders


def update_order_status(
    db: Session, order_id: int, status: models.OrderStatusEnum
) -> models.Order:
    order = db.query(models.Order).filter(models.Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    try:
        order.status = status
        db.commit()
        db.refresh(order)
        return order

    except:
        db.rollback()
        raise
