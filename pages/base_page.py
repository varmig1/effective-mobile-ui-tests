from playwright.sync_api import Page

class BasePage:
    """Базовый класс для всех страниц"""
    
    def __init__(self, page: Page):
        self.page = page
    
    def goto(self, url: str):
        """Метод перехода по URL"""
        self.page.goto(url)
    
    def get_title(self) -> str:
        """Метод получения заголовка страницы"""
        return self.page.title()
    
    def get_url(self) -> str:
        """Метод Получения текущего URL"""
        return self.page.url