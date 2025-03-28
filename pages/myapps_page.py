# pages/login_page.py
from playwright.sync_api import Page
class HomePage:
    def __init__(self, page: Page):
        self.page = page

    # Locators
    MENU = "#body > div.topRow > div.connection_info"
