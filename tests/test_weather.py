# Exercise

# 1. Open the OpenWeatherMap homepage.
# 2. Search for a city (e.g., "Bengaluru").
# 3. Select the city from the search suggestions.
# 4. Verify that the correct city profile loads and extract the live temperature text

import pytest 
from playwright.sync_api import Page,expect

def test_check_city_weather(page: Page):
    # Navigate to home page 
    page.goto("https://openweathermap.org/")

    # 2. Assert that the page title contains expected branding
    expect(page).to_have_title("Current weather and forecast")

    #3. Locate the search using placholder text , input and press enter
    search_input = page.get_by_placeholder("Search city")
    expect(search_input).to_be_visible()
    search_input.fill("Bengaluru")
    search_input.press("Enter")


    #4.click on the first match drop down suggestion from the auto complete box
    suggestion_item = page.locator(".search-dropdown-menu li").first
    suggestion_item.click()

    #5 wait for weather widget matching the city name 
    city_heading = page.locator(".current-container h2")
    expect(city_heading).to_contain_text("Bengaluru",timeout=1000)

    #6 xtract and display live temperature 
    temperature = page.locator(".current-container .heading").inner_text()
    print(f"\n successully loaded weather, weather of bengalur is : {temperature}")
