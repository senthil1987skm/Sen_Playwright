import re
import pytest


@pytest.mark.smoke
def test_login_page_loads(page, base_url):
    page.goto(base_url)
    assert page.locator("#login-button").is_visible()
    assert page.locator(".login_logo").inner_text() == "Swag Labs"


@pytest.mark.smoke
def test_standard_user_can_log_in(page, base_url):
    page.goto(base_url)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_selector(".inventory_list")
    assert re.search(r"/inventory\.html$", page.url)


@pytest.mark.smoke
def test_locked_out_user_is_blocked(page, base_url):
    page.goto(base_url)
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    error = page.locator("[data-test='error']")
    assert error.is_visible()
    assert "locked out" in error.inner_text().lower()


@pytest.mark.smoke
def test_inventory_lists_six_products(logged_in_page):
    items = logged_in_page.locator(".inventory_item")
    assert items.count() == 6
