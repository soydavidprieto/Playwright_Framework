# abilities/browser.py
from playwright.sync_api import Page

class BrowseTheWeb:
    def __init__(self, page: Page):
        self.page = page
