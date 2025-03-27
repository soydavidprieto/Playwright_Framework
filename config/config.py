# config/config.py
from dataclasses import dataclass
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

@dataclass
class Settings:
    env: str
    base_url: str
    headless: bool
    timeout: int

    @staticmethod
    def from_env() -> "Settings":
        return Settings(
            env=os.getenv("ENV", "staging"),
            base_url=os.getenv("BASE_URL", "http://localhost:3000"),
            headless=os.getenv("HEADLESS", "true").lower() == "true",
            timeout=int(os.getenv("TIMEOUT", "10000")),
        )

# Global settings instance
settings = Settings.from_env()