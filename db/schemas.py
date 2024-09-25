from pydantic import BaseModel
from typing import List

from datetime import datetime


# Schemas for Product
class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    stock: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True


# Schemas for Product
class OrderItemBase(BaseModel):
    product_id: int
    quantity: int


class OrderCreate(BaseModel):
    items: List[OrderItemBase]


class Order(BaseModel):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
