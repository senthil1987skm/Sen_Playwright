import pytest

BASE_URL = "https://www.saucedemo.com"

STANDARD_USER = "standard_user"
LOCKED_USER = "locked_out_user"
PASSWORD = "secret_sauce"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def logged_in_page(page):
    """Returns a page already logged in as the standard user."""
    page.goto(BASE_URL)
    page.fill("#user-name", STANDARD_USER)
    page.fill("#password", PASSWORD)
    page.click("#login-button")
    page.wait_for_selector(".inventory_list")
    return page
