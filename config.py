from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Main database
    sqlalchemy_database_url: str
    postgres_user: str
    postgres_password: str
    postgress_db: str

    # Test database
    sqlalchemy_database_url_test: str
    postgres_user_test: str
    postgres_password_test: str
    postgress_db_test: str

    # API
    api_prefix: str


    class Config:
        env_file = ".env"


settings = Settings()