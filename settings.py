from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str
    CHAT_ID: str

    class Config:
        env_file = ".env"

settings = Settings()