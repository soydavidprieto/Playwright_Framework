import requests
from config.config import settings

class GetAPI:
    def __init__(self):
        self.base_url_api = settings.base_url_api

    def get_character(self, page=1):
        endpoint = f"{self.base_url_api}/character"
        params = {"page": page}
        return requests.get(endpoint, params=params)