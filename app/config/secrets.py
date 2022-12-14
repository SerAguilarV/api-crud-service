from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_URI: str = "mongodb://localhost:27017"
    DATABASE: str = "test"


settings = Settings()
