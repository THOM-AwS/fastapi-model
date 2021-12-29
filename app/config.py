from pydantic import BaseSettings

class Settings(BaseSettings):
    access_token_expire_minutes: int
    database_hostname: str
    database_username: str
    database_password: str
    database_name: str
    database_port: int
    secret_key: str
    algorithm: str

    class Config:
        env_prefix = ""
        case_sentive = False
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()