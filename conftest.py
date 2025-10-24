import pytest
from playwright.sync_api import Page, sync_playwright
from pages.main_page import MainPage
import os

@pytest.fixture(scope="session")
def browser():
    """Фикстура для браузера"""
    from playwright.sync_api import sync_playwright
    
    with sync_playwright() as p:
        is_headless = os.getenv('DISPLAY') is None or os.getenv('DOCKER_RUN') == 'true'
        
        browser = p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-dev-shm-usage']
        )
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    """Фикстура для создания новой страницы"""
    context = browser.new_context()
    new_page = context.new_page()
    new_page.set_default_timeout(30000)
    yield new_page
    context.close()

@pytest.fixture
def main_page(page: Page):
    """Фикстура для главной страницы"""
    main_page = MainPage(page)
    main_page.goto_main_page()
    return main_page