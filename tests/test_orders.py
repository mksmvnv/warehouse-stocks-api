from fastapi.testclient import TestClient


def test_create_order(client: TestClient) -> None:
    test_product = client.post(
        "/products/",
        json={
            "name": "Beer",
            "description": "Beer from the market",
            "price": 149,
            "stock": 100,
        },
    )

    response = client.post(
        "/orders/",
        json={"items": [{"product_id": test_product.json()["id"], "quantity": 10}]},
    )

    assert response.status_code == 200
    assert response.json()["id"] is not None
    assert response.json()["status"] == "в процессе"
    assert "created_at" in response.json()


def test_create_order_not_found(client: TestClient) -> None:
    test_product_id = 1000
    response = client.post(
        "/orders/",
        json={"items": [{"product_id": test_product_id, "quantity": 10}]},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == f"Product with id {test_product_id} not found"


def test_create_order_not_enough_stock(client: TestClient) -> None:
    test_product = client.post(
        "/products/",
        json={
            "name": "Milk",
            "description": "Milk from the farm",
            "price": 88.99,
            "stock": 5,
        },
    )

    response = client.post(
        "/orders/",
        json={"items": [{"product_id": test_product.json()["id"], "quantity": 10}]},
    )

    assert response.status_code == 400
    assert (
        response.json()["detail"]
        == f"Not enough stock for product with id {test_product.json()['id']}"
    )


def test_get_order(client: TestClient) -> None:
    test_product = client.post(
        "/products/",
        json={
            "name": "Watermelon",
            "description": "Watermelon from the foreign country",
            "price": 1299.99,
            "stock": 10,
        },
    )

    test_order = client.post(
        "/orders/",
        json={"items": [{"product_id": test_product.json()["id"], "quantity": 3}]},
    )

    response = client.get(f"/orders/{test_order.json()['id']}")

    assert response.status_code == 200
    assert response.json()["id"] == test_order.json()["id"]
    assert response.json()["status"] == "в процессе"
    assert "created_at" in response.json()


def test_get_order_not_found(client: TestClient) -> None:
    test_order_id = 1000
    response = client.get(f"/orders/{test_order_id}")

    assert response.status_code == 404
    assert response.json()["detail"] == f"Order with id {test_order_id} not found"


def test_get_orders(client: TestClient) -> None:
    test_product = client.post(
        "/products/",
        json={
            "name": "Sosusages",
            "description": "Sosusages from the market",
            "price": 399.99,
            "stock": 100,
        },
    )

    test_orders = [
        {
            "items": [{"product_id": test_product.json()["id"], "quantity": 3}],
        },
        {
            "items": [{"product_id": test_product.json()["id"], "quantity": 5}],
        },
    ]

    for test_order in test_orders:
        client.post("/orders/", json=test_order)

    response = client.get("/orders/")

    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_orders_not_found(client: TestClient) -> None:
    response = client.get("/orders/")

    assert response.status_code == 404
    assert response.json()["detail"] == "Orders not found"


def test_update_order_status(client: TestClient) -> None:
    test_product = client.post(
        "/products/",
        json={
            "name": "Chicken",
            "description": "Chicken from the farm",
            "price": 288.99,
            "stock": 10,
        },
    )

    test_order = client.post(
        "/orders/",
        json={"items": [{"product_id": test_product.json()["id"], "quantity": 3}]},
    )

    status = "отправлен"

    response = client.patch(f"/orders/{test_order.json()['id']}/status?status={status}")

    print(response.json())

    assert response.status_code == 200
    assert response.json()["status"] == "отправлен"


def test_update_order_status_not_found(client: TestClient) -> None:
    test_order_id = 1000
    status = "отправлен"

    response = client.patch(f"/orders/{test_order_id}/status?status={status}")

    assert response.status_code == 404
    assert response.json()["detail"] == f"Order with id {test_order_id} not found"
