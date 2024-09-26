from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from db import schemas
from db.connect import get_db

from controllers import product_controller


router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return product_controller.create_product(db, product)


@router.get("/", response_model=list[schemas.Product])
def list_products(db: Session = Depends(get_db)):
    return product_controller.get_products(db)


@router.get("/{product_id}", response_model=schemas.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return product_controller.get_product(db, product_id)


@router.put("/{product_id}", response_model=schemas.Product)
def update_product(
    product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)
):
    return product_controller.update_product(db, product_id, product)


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_controller.delete_product(db, product_id)
    return {"message": "Product deleted"}
