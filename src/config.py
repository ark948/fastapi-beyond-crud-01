from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from os import getenv



load_dotenv()



SECRET_KEY = getenv("SECRET_KEY")
DATABASE_URL = getenv("DB_URL")


class Settings(BaseSettings):
    DB_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )




Config = Settings()