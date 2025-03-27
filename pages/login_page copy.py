# pages/login_page.py
from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def fill_credentials(self, username: str, password: str):
        self.page.fill("#username", username)
        self.page.fill("#password", password)

    def submit(self):
        self.page.click("[data-test='signin-submit']")
