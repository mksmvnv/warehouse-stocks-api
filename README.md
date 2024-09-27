# Warehouse Stocks API 📦

![Static Badge](https://img.shields.io/badge/Python-3\.12-blue)

This is an implementation of a test API for warehouse stock control and orders.

## How to Run

### Step 1: Create Environment Variables

Create a **.env** file in the root directory of your project and add the following environment variables:

- `sqlalchemy_database_url`=postgresql://db_user:db_password@db_host:db_port/db_name
- `postgres_user`=db_user
- `postgres_password`=db_password
- `postgress_db`=db_name

- `sqlalchemy_database_url_test`=postgresql://db_test_user:db_test_password@db_test_host:db_test_port/db_test_name
- `postgres_user_test`=db_test_user
- `postgres_password_test`=db_test_password
- `postgress_db_test`=db_test_name

- `api_prefix`=secret_api_prefix

### Step 2: Create a Server Session

Before build containers, create a session on the server:\

```
tmux new -s warehouse-stocks-api
```

### Step 3: Run the App with Docker

To build and run the app using Docker, execute:\

```
docker compose up -d
```

## How to Use

Now that the server is running, you can test the available endpoints of your API. To do this, open Postman or navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to view the automatic Swagger documentation.

#### Endpoints for Products:

- *Create Product*:

  `POST /secret_prefix/products`
  
  Use this endpoint to add a new product to the system.

- *Get List of Products*:
  
  `GET /secret_prefix/products`
  
  This endpoint returns a list of all products.

- *Get Product Information by ID*:
  
  `GET /secret_prefix/products/{id}`
  
  Retrieve information about a specific product by replacing `{id}` with the product's identifier.

- *Update Product Information*:
  
  `PUT /secret_prefix/products/{id}`
  
  This endpoint allows you to update product information. Be sure to replace `{id}` with the desired identifier.

- *Delete Product*:
  
  `DELETE /secret_prefix/products/{id}`
  
  Remove a product by replacing `{id}` with the identifier of the product to be deleted.

#### Endpoints for Orders:

- *Create Order*:
  
  `POST /secret_prefix/orders`
  
  Use this endpoint to create a new order.

- *Get List of Orders*:
  
  `GET /secret_prefix/orders`
  
  This endpoint returns a list of all orders.

- *Get Order Information by ID*:
  
  `GET /secret_prefix/orders/{id}`
  
  Retrieve information about a specific order by replacing `{id}` with the order's identifier.

- *Update Order Status*:
  
  `PATCH /secret_prefix/orders/{id}/status`
  
  Use this endpoint to update the status of an order by replacing `{id}` with the order's identifier.


### Test these endpoints to ensure your API is functioning correctly! 💫
