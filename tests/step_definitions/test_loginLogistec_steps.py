import yaml
from pytest_bdd import scenarios, given, when, then, parsers
from pages.loginLogistec_page import LoginPage
from pages.myapps_page import HomePage
from utils.actor import Actor
from abilities.browser import BrowseTheWeb
from tasks.loginLogistec_task import Login
from questions.element_visible import ElementVisible
from config.config import settings

scenarios("../features/loginLogistec.feature")

# Cargar YAML de usuarios
with open("resources/data/usersLogistec.yaml", "r") as f:
    user_data = yaml.safe_load(f)["users"]

@given("the user is on the login page")
def visit_login(page):
    page.goto(settings.base_url_logistec)

@when(parsers.parse('they log in as "{user_type}"'))
def login_as(page, user_type):
    user = Actor("User").can(BrowseTheWeb(page))

    # Elegir usuario desde YAML o fallback al entorno
    creds = user_data.get(user_type, {
        "username": settings.login_user,
        "password": settings.login_pass
    })

    user.attempts_to(Login(creds["username"], creds["password"]))

@then(parsers.parse('the system should respond appropriately for "{user_type}"'))
def response_check(page, user_type):
    actor = Actor("Verifier").can(BrowseTheWeb(page))
    loginLogistec_page = LoginPage(page)
    myapps_page = HomePage(page)

    if user_type == "invalid":
        actor.should_see_that(ElementVisible(LoginPage.ERROR_ALERT))
    else:
        actor.should_see_that(ElementVisible(HomePage.MENU))