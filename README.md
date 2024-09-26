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


### Your API is now ready to use. Enjoy! 💫
