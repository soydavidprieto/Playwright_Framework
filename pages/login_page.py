# pages/login_page.py
from playwright.sync_api import Page
class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    # Locators
    USERNAME_FIELD = 'input[name="username"]'
    PASSWORD_FIELD = 'input[name="password"]'
    SUBMIT_BUTTON = 'button[type="submit"]'
    DASHBOARD_HEADER = 'div.oxd-topbar-header-title'
    ERROR_ALERT = '#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > div > div.oxd-alert.oxd-alert--error > div.oxd-alert-content.oxd-alert-content--error'

    def navigate(self, url: str):
        self.page.goto(url)

    def fill_credentials(self, username: str, password: str):
        self.page.fill(self.USERNAME_FIELD, username)
        self.page.fill(self.PASSWORD_FIELD, password)

    def submit(self):
        self.page.click(self.SUBMIT_BUTTON)
