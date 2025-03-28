# tests/e2e/test_login.py
from utils.actor import Actor
from abilities.browser import BrowseTheWeb
from tasks.login_task import Login
from questions.element_visible import ElementVisible

def test_user_can_login(page):
    user = Actor("Admin").can(BrowseTheWeb(page))
    user.attempts_to(Login("Admin", "admin123"))
    user.should_see_that(ElementVisible("div.oxd-topbar-header-title"))
