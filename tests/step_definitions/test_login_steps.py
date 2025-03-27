# tests/step_definitions/test_login_steps.py
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from utils.actor import Actor
from abilities.browser import BrowseTheWeb
from tasks.login_task import Login
from questions.element_visible import ElementVisible
from config.config import settings

scenarios("../features/login.feature")

@pytest.fixture
def actor(page):
    return Actor("Admin").can(BrowseTheWeb(page))

@given("que el usuario accede a la página de login")
def go_to_login(actor):
    page = actor.ability_to(BrowseTheWeb).page
    page.goto(settings.base_url + "/signin")

@when(parsers.parse('ingresa el usuario "{username}" y la contraseña "{password}"'))
def login(actor, username, password):
    actor.attempts_to(Login(username, password))

@then("debería ver el dashboard")
def see_dashboard(actor):
    actor.should_see_that(ElementVisible("[data-test='sidenav-user-full-name']"))