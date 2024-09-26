from fastapi import FastAPI

from db.connect import init_db

from routers import order_router, product_router


app = FastAPI()

init_db()

app.include_router(product_router.router)
app.include_router(order_router.router)
