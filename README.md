# Warehouse Stocks API 📦

![Static Badge](https://img.shields.io/badge/Python-3\.12-blue)

This is an implementation of a test API for warehouse stock control and orders.

## How to Run

### Step 1: Create Environment Variables

Create a **.env** file in the root directory of your project and add the following environment variables:

- `SQLALCHEMY_DATABASE_URL`=postgresql://db_user:db_password@db_host:db_port/db_name
- `POSTGRES_USER`=db_user
- `POSTGRES_PASSWORD`=db_password
- `POSTGRES_DB`=db_name

- `SQLALCHEMY_DATABASE_URL_TEST`=postgresql://db_test_user:db_test_password@db_test_host:db_test_port/db_test_name
- `POSTGRES_USER_TEST`=db_test_user
- `POSTGRES_PASSWORD_TEST`=db_test_password
- `POSTGRES_DB_TEST`=db_test_name

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

### Step 4: Testing the API

Now that the server is running, you can test the available endpoints of your API. To do this, open Postman or navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to view the automatic Swagger documentation.

#### Endpoints for Products:
- **Create Product**:  
  `POST /products`  
  Use this endpoint to add a new product to the system.

- **Get List of Products**:  
  `GET /products`  
  This endpoint returns a list of all products.

- **Get Product Information by ID**:  
  `GET /products/{id}`  
  Retrieve information about a specific product by replacing `{id}` with the product's identifier.

- **Update Product Information**:  
  `PUT /products/{id}`  
  This endpoint allows you to update product information. Be sure to replace `{id}` with the desired identifier.

- **Delete Product**:  
  `DELETE /products/{id}`  
  Remove a product by replacing `{id}` with the identifier of the product to be deleted.

#### Endpoints for Orders:
- **Create Order**:  
  `POST /orders`  
  Use this endpoint to create a new order.

- **Get List of Orders**:  
  `GET /orders`  
  This endpoint returns a list of all orders.

- **Get Order Information by ID**:  
  `GET /orders/{id}`  
  Retrieve information about a specific order by replacing `{id}` with the order's identifier.

- **Update Order Status**:  
  `PATCH /orders/{id}/status`  
  Use this endpoint to update the status of an order by replacing `{id}` with the order's identifier.

### Test these endpoints to ensure your API is functioning correctly! 💫
