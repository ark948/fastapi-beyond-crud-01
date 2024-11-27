from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from os import getenv


load_dotenv()


SECRET_KEY = getenv("SECRET_KEY")
DATABASE_URL = getenv("DB_URL")


class Settings(BaseSettings):
    DB_URL: str
    JWT_SECRET: str
    SECRET_KEY: str
    JWT_ALGORITHM: str
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    DOMAIN: str
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


Config = Settings()
