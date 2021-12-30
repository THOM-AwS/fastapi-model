from pydantic import BaseSettings
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=Path("~/projects/pythonapi/app/.env"))

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = '~/projects/pythonapi/app/.env'
        orm_mode = True

settings = Settings()


