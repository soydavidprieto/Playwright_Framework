# conftest.py
import pytest
from playwright.sync_api import sync_playwright, Browser, Page
from config.config import settings

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance) -> Browser:
    return playwright_instance.chromium.launch(headless=settings.headless)

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        yield browser
        browser.close()
    
@pytest.fixture(scope="function")
def context(browser):
    # Desactiva validación de certificado SSL
    return browser.new_context(ignore_https_errors=True)