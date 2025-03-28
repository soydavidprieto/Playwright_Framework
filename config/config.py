# config/config.py
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    def __init__(self):
        self.env = os.getenv("ENV", "staging")
        self.base_url = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com")
        self.base_url_logistec = os.getenv("BASE_URL_LOGISTEC", "https://myapps.dev.logistec.com/web/dev/apps/myapps/v2.14.25/mainfile.php?")
        self.base_url_api = os.getenv("BASE_URL_API", "https://rickandmortyapi.com/api")
        self.headless = os.getenv("HEADLESS", "true").lower() == "true"
        self.timeout = int(os.getenv("TIMEOUT", "10000"))
        self.login_user = os.getenv("LOGIN_USER")
        self.login_pass = os.getenv("LOGIN_PASS")

settings = Settings()