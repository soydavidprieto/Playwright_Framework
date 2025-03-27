# tasks/login_task.py
from config.config import settings
from pages.login_page import LoginPage
from abilities.browser import BrowseTheWeb

class Login:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def perform_as(self, actor):
        page = actor.ability_to(BrowseTheWeb).page
        login_page = LoginPage(page)
        login_page.navigate(settings.base_url + "/signin")
        login_page.fill_credentials(self.username, self.password)
        login_page.submit()
