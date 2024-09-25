import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from dotenv import find_dotenv, load_dotenv
from pydantic import PostgresDsn, Field, MongoDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')
    db: str = Field(..., alias="DB")
    db_host: str = Field(..., alias="HOST")
    db_port: str = Field(..., alias="PORT")
    db_name: str = Field(..., alias="DB_NAME")

    @property
    def database_url(self) -> MongoDsn:
        """ URL для подключения (DSN)"""
        return f"{self.db}://{self.db_host}:{self.db_port}"


settings = Settings()
