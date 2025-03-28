# pages/login_page.py
from playwright.sync_api import Page
class HomePage:
    def __init__(self, page: Page):
        self.page = page

    # Locators
    MENU = '#body > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(1) > a:nth-child(1)'

    def navigate(self, url: str):
        self.page.goto(url)