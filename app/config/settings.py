from pydantic import BaseSettings


class Base(BaseSettings):

    DB_DBNAME: str = "todo-list"
    DB_USERNAME: str = "root"
    DB_PASSWORD: str = "toor"
    DB_URL: str = "localhost:5432"
    SQLALCHEMY_URL: str = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_URL}/{DB_DBNAME}"
    DB_ECHO: bool = False


class DevSettings(Base):
    ENV: str = "dev"


def __get_settings() -> BaseSettings:
    return DevSettings()


settings: Base = __get_settings()
