import pytest


@pytest.mark.regression
def test_add_single_item_to_cart(logged_in_page):
    page = logged_in_page
    page.click("#add-to-cart-sauce-labs-backpack")
    badge = page.locator(".shopping_cart_badge")
    assert badge.inner_text() == "1"


@pytest.mark.regression
def test_add_and_remove_item_updates_badge(logged_in_page):
    page = logged_in_page
    page.click("#add-to-cart-sauce-labs-backpack")
    assert page.locator(".shopping_cart_badge").inner_text() == "1"
    page.click("#remove-sauce-labs-backpack")
    assert page.locator(".shopping_cart_badge").count() == 0


@pytest.mark.regression
def test_sort_products_price_low_to_high(logged_in_page):
    page = logged_in_page
    page.select_option(".product_sort_container", "lohi")
    prices = page.locator(".inventory_item_price").all_inner_texts()
    values = [float(p.replace("$", "")) for p in prices]
    assert values == sorted(values)


@pytest.mark.regression
def test_sort_products_name_z_to_a(logged_in_page):
    page = logged_in_page
    page.select_option(".product_sort_container", "za")
    names = page.locator(".inventory_item_name").all_inner_texts()
    assert names == sorted(names, reverse=True)


@pytest.mark.regression
def test_full_checkout_flow(logged_in_page):
    page = logged_in_page
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.click("#checkout")
    page.fill("#first-name", "Meena")
    page.fill("#last-name", "QA")
    page.fill("#postal-code", "560001")
    page.click("#continue")
    page.click("#finish")
    confirmation = page.locator(".complete-header")
    assert "Thank you" in confirmation.inner_text()


@pytest.mark.regression
def test_checkout_blocks_missing_fields(logged_in_page):
    page = logged_in_page
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.click("#checkout")
    page.click("#continue")
    error = page.locator("[data-test='error']")
    assert error.is_visible()
