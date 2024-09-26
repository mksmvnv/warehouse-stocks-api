from fastapi import HTTPException

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from db import models, schemas


def create_product(db: Session, product: schemas.ProductCreate) -> models.Product:
    # Validate product name
    if not product.name:
        raise HTTPException(status_code=400, detail="Product name cannot be empty")

    # Create new product
    new_product = models.Product(**product.model_dump())

    try:
        db.add(new_product)
        db.commit()
        db.refresh(new_product)

        return new_product

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating product: {e}")


def get_product(db: Session, product_id: int) -> models.Product:
    # Check if product exists
    db_product = (
        db.query(models.Product).filter(models.Product.id == product_id).first()
    )

    if not db_product:
        raise HTTPException(
            status_code=404, detail=f"Product with id {product_id} not found"
        )

    return db_product


def get_products(db: Session) -> list[models.Product]:
    # Check if products exist
    db_products = db.query(models.Product).all()

    if not db_products:
        raise HTTPException(status_code=404, detail="Products not found")

    return db_products


def update_product(
    db: Session, product_id: int, product: schemas.ProductUpdate
) -> models.Product:
    # Check if product exists
    db_product = get_product(db, product_id)

    if not db_product:
        raise HTTPException(
            status_code=404, detail=f"Product with id {product_id} not found"
        )

    # Update product
    for key, value in product.model_dump().items():
        setattr(db_product, key, value)

    try:
        db.commit()
        db.refresh(db_product)

        return db_product

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating product: {e}")


def delete_product(db: Session, product_id: int) -> None:
    # Check if product exists
    db_product = get_product(db, product_id)

    if not db_product:
        raise HTTPException(
            status_code=404, detail=f"Product with id {product_id} not found"
        )

    # Check if product is referenced in existing orders
    order_items_count = (
        db.query(models.OrderItem)
        .filter(models.OrderItem.product_id == product_id)
        .count()
    )

    if order_items_count > 0:
        raise HTTPException(
            status_code=400,
            detail=f"Cannot delete product with id {product_id}. It is referenced in existing orders",
        )

    try:
        # Delete product
        db.delete(db_product)
        db.commit()

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting product: {e}")
