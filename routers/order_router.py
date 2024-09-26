from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from db import models, schemas
from db.connect import get_db

from controllers import order_controller


router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return order_controller.create_order(db, order)


@router.get("/", response_model=list[schemas.Order])
def list_orders(db: Session = Depends(get_db)):
    return order_controller.get_orders(db)


@router.get("/{order_id}", response_model=schemas.Order)
def get_order(order_id: int, db: Session = Depends(get_db)):
    return order_controller.get_order(db, order_id)


@router.patch("/{order_id}/status", response_model=schemas.Order)
def update_order_status(
    order_id: int, status: models.OrderStatusEnum, db: Session = Depends(get_db)
):
    return order_controller.update_order_status(db, order_id, status)
