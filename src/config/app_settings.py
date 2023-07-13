from pydantic import  HttpUrl, PostgresDsn
from pydantic.v1 import BaseSettings


class AppSettings(BaseSettings):
    project_name: str = "Easy CMS"
    project_host: str | HttpUrl = "127.0.0.1"
    project_port: int = 8080

    project_db: PostgresDsn | str = (
        "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
    )

    project_shortener: str = "csl"
    echo: bool = True
    secret_key: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

    is_debug: bool = False

    # class Config:
    #     env_file = ".env"


app_settings = AppSettings()
