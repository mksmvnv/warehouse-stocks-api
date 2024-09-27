from fastapi import FastAPI

from db.connect import init_db

from routers import order_router, product_router

from config import settings


app = FastAPI()

init_db()

app.include_router(product_router.router, prefix=settings.api_prefix)
app.include_router(order_router.router, prefix=settings.api_prefix)
