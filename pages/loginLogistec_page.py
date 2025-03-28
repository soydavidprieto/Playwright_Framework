# Login Logistec

from playwright.sync_api import Page
class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    # Locators
    USERNAME_FIELD = "#txt_username"
    PASSWORD_FIELD = "#txt_password"
    SUBMIT_BUTTON = "#submit"
    ERROR_ALERT = '#form_login > fieldset > table > tbody > tr:nth-child(3) > td > span'

    def navigate(self, url: str):
        self.page.goto(url)

    def fill_credentials(self, username: str, password: str):
        self.page.fill(self.USERNAME_FIELD, username)
        self.page.fill(self.PASSWORD_FIELD, password)

    def submit(self):
        self.page.click(self.SUBMIT_BUTTON)
