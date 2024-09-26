from fastapi.testclient import TestClient


def test_create_product(client: TestClient) -> None:
    response = client.post(
        "/products/",
        json={
            "name": "Beer",
            "description": "Beer from the market",
            "price": 149,
            "stock": 100,
        },
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Beer"
    assert response.json()["description"] == "Beer from the market"
    assert response.json()["price"] == 149
    assert response.json()["stock"] == 100


def test_create_product_with_empty_name(client: TestClient) -> None:
    response = client.post(
        "/products/",
        json={
            "name": "",
            "description": "Test Description",
            "price": 299,
            "stock": 100,
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Product name cannot be empty"


def test_get_product(client: TestClient) -> None:
    test_product = client.post(
        "/products/",
        json={
            "name": "Milk",
            "description": "Milk from the farm",
            "price": 99.99,
            "stock": 1500,
        },
    )

    response = client.get(f"/products/{test_product.json()['id']}")

    assert response.status_code == 200
    assert response.json()["name"] == "Milk"
    assert response.json()["description"] == "Milk from the farm"
    assert response.json()["price"] == 99.99
    assert response.json()["stock"] == 1500


def test_get_product_not_found(client: TestClient) -> None:
    test_product_id = 1000
    response = client.get(f"/products/{test_product_id}")

    assert response.status_code == 404
    assert response.json()["detail"] == f"Product with id {test_product_id} not found"


def test_get_products(client: TestClient) -> None:
    test_products = [
        {
            "name": "Tomatoes",
            "description": "Tomatoes from the farm",
            "price": 99.99,
            "stock": 1500,
        },
        {
            "name": "Potatoes",
            "description": "Potatoes from the farm",
            "price": 59.99,
            "stock": 500,
        },
    ]

    for test_product in test_products:
        client.post("/products/", json=test_product)

    response = client.get("/products/")

    assert response.status_code == 200
    assert len(response.json()) == len(test_products)


def test_get_products_not_found(client: TestClient) -> None:
    response = client.get("/products/")

    assert response.status_code == 404
    assert response.json()["detail"] == "Products not found"


def test_update_product(client: TestClient) -> None:
    test_product = client.post(
        "/products/",
        json={
            "name": "Watermelon",
            "description": "Watermelon from the foreign country",
            "price": 99.99,
            "stock": 1500,
        },
    )

    response = client.put(
        f"/products/{test_product.json()['id']}",
        json={
            "name": "Updated watermelon",
            "description": "Updated watermelon from the foreign country",
            "price": 199.99,
            "stock": 2500,
        },
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated watermelon"
    assert (
        response.json()["description"] == "Updated watermelon from the foreign country"
    )
    assert response.json()["price"] == 199.99
    assert response.json()["stock"] == 2500


def test_update_product_not_found(client: TestClient) -> None:
    test_product_id = 1000
    response = client.put(
        f"/products/{test_product_id}",
        json={
            "name": "Updated watermelon",
            "description": "Updated watermelon from the foreign country",
            "price": 199.99,
            "stock": 2500,
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == f"Product with id {test_product_id} not found"


def test_delete_product(client: TestClient) -> None:
    test_product = client.post(
        "/products/",
        json={
            "name": "Sousages",
            "description": "Sousages from the market",
            "price": 299.99,
            "stock": 150,
        },
    )

    response = client.delete(f"/products/{test_product.json()['id']}")

    assert response.status_code == 200
    assert response.json()["message"] == "Product deleted"


def test_delete_product_with_order(client: TestClient) -> None:
    test_product = client.post(
        "/products/",
        json={
            "name": "Chicken",
            "description": "Chicken from the farm",
            "price": 499,
            "stock": 100,
        },
    )

    test_order = client.post(
        "/orders/",
        json={"items": [{"product_id": test_product.json()["id"], "quantity": 10}]},
    )

    response = client.delete(f"/products/{test_product.json()['id']}")

    assert response.status_code == 400
    assert (
        response.json()["detail"]
        == f"Cannot delete product with id {test_product.json()['id']}. It is referenced in existing orders"
    )
