import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    TOKEN: str = os.getenv("TOKEN", "")
    WEBHOOK_URL: str = os.getenv("WEBHOOK_URL", "")


settings = Settings()
