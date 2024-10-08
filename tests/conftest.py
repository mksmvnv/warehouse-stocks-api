import pytest

from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app

from db.models import Base
from db.connect import get_db

from config import settings

SQLALCHEMY_DATABASE_URL_TEST = settings.sqlalchemy_database_url_test

engine_test = create_engine(SQLALCHEMY_DATABASE_URL_TEST)
SessionLocalTest = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)


def override_get_db():
    db = SessionLocalTest()

    try:
        yield db

    finally:
        db.close()


@pytest.fixture(autouse=True)
def test_init_db():
    Base.metadata.create_all(bind=engine_test)
    yield
    Base.metadata.drop_all(bind=engine_test)


@pytest.fixture
def client():
    app.dependency_overrides[get_db] = override_get_db

    return TestClient(app)
