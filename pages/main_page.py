from .base_page import BasePage

class MainPage(BasePage):
    """
    Класс, который содержит локаторы и методы для взаимодействия с элементами страницы
    """
    
    def __init__(self, page):
        super().__init__(page)
        
        # ЛОКАТОРЫ ЭЛЕМЕНТОВ
        
        # Header
        self.main = "a[href='#main']"                           # Логотип/ссылка на главную
        self.about_link = "a[href='#about']"                    # Ссылка "О нас"
        self.services_link = "a[href='#moreinfo']"              # Ссылка "Услуги"
        self.projects_link = "a[href='#cases']"                 # Ссылка "Проекты"
        self.reviews_link = "a[href='#Reviews']"                # Ссылка "Отзывы"
        self.contacts_link = "a[href='#contacts']"              # Ссылка "Контакты"
        self.specialists_link = "a[href='#specialists']"        # Ссылка "Выбрать специалиста"
        
        # Кнопки на основной странице
        self.details_button = "a[href='#moreinfo']"             # Кнопка "Подробнее"
        self.cooperation_button = "a[href='#contacts']"         # Кнопка "Оставить заявку на сотрудничество"
        
        # Внешние ссылки и контакты
        self.telegram_support_link = "a[href='https://t.me/assistant_em']"    # ТГ поддержка
        self.telegram_link = "a[href='https://t.me/krasnikova_d']"            # Личный Telegram
        self.email_link = "a[href='mailto:dariia.krasnikova@effectivemobile.ru']"  # Email
        self.privacy_link_1 = "a[href='https://effective-mobile.ru/privacy']" # Политика конфиденциальности (1)
        
        # Футер
        self.privacy_link_2 = "a[href='https://effective-mobile.ru/privacy']" # Политика конфиденциальности (2)
    
    # === МЕТОДЫ НАВИГАЦИИ ===
    
    def goto_main_page(self):
        """Переход на главную страницу effective-mobile.ru"""
        self.goto("https://effective-mobile.ru")
        self.page.wait_for_timeout(3000)
    
    # === МЕТОДЫ КЛИКОВ ПО НАВИГАЦИИ ===
    
    def click_main(self):
        """Клик по логотипу/ссылке на главную страницу"""
        self.page.eval_on_selector(self.main, "element => element.click()")
    
    def click_about_link(self):  
        """Клик по ссылке 'О нас' в навигации"""
        self.page.eval_on_selector(self.about_link, "element => element.click()")
    
    def click_services_link(self):
        """Клик по ссылке 'Услуги' в навигации"""
        self.page.eval_on_selector(self.services_link, "element => element.click()")
        
    def click_projects_link(self):
        """Клик по ссылке 'Проекты' в навигации"""
        self.page.eval_on_selector(self.projects_link, "element => element.click()")
        
    def click_reviews_link(self):
        """Клик по ссылке 'Отзывы' в навигации"""
        self.page.eval_on_selector(self.reviews_link, "element => element.click()")

    def click_contacts_link(self):
        """Клик по ссылке 'Контакты' в навигации"""
        self.page.eval_on_selector(self.contacts_link, "element => element.click()")
        
    def click_specialists_link(self):
        """Клик по ссылке 'Выбрать специалиста' в навигации"""
        self.page.eval_on_selector(self.specialists_link, "element => element.click()")

    def click_details_button(self):
        """Клик по кнопке 'Подробнее' на главной странице"""
        self.page.eval_on_selector(self.details_button, "element => element.click()")

    def click_cooperation_button(self):
        """Клик по кнопке 'Оставить заявку на сотрудничество'"""
        self.page.eval_on_selector(self.cooperation_button, "element => element.click()")
  
    # === МЕТОДЫ КЛИКОВ ПО ВНЕШНИМ ССЫЛКАМ ===
    
    def click_telegram_support_link(self):
        """Клик по ссылке 'ТГ поддержка' (открывает Telegram)"""
        self.page.eval_on_selector(self.telegram_support_link, "element => element.click()")
  
    def click_telegram_link(self):
        """Клик по ссылке 'Telegram' (открывает Telegram)"""
        self.page.eval_on_selector(self.telegram_link, "element => element.click()")

    def click_email_link(self):
        """Клик по email ссылке (открывает почтовый клиент)"""
        self.page.eval_on_selector(self.email_link, "element => element.click()")

    def click_privacy_link_1(self):
        """Клик по первой ссылке 'Политика конфиденциальности'"""
        self.page.eval_on_selector(self.privacy_link_1, "element => element.click()")

    def click_privacy_link_2(self):
        """Клик по второй ссылке 'Политика конфиденциальности' (в футере)"""
        self.page.eval_on_selector(self.privacy_link_2, "element => element.click()")
  
    # === МЕТОДЫ ПРОВЕРКИ ВИДИМОСТИ РАЗДЕЛОВ ===
    
    def is_main(self):
        """Проверка что главная страница видима (по заголовку)"""
        return self.page.is_visible("text=Разработка мобильных приложений")
    
    def is_about_section_visible(self):
        """Проверка что раздел 'О нас' видима после перехода"""
        return self.page.is_visible("text=Effective Mobile — это команда экспертов")
    
    def is_services_section_visible(self):
        """Проверка что раздел 'Услуги' видима после перехода"""
        return self.page.is_visible("text=АУТСТАФФИНГ IT-персонала и специалистов")
    
    def is_projects_section_visible(self):
        """Проверка что раздел 'Проекты' видима после перехода"""
        return self.page.is_visible("#rec572838727")
    
    def is_reviews_section_visible(self):
        """Проверка что раздел 'Отзывы' видима после перехода"""
        return self.page.is_visible("text=ОТЗЫВЫ КЛИЕНТОВ")
    
    def is_contacts_section_visible(self):
        """Проверка что раздел 'Контакты' видима после перехода"""
        return self.page.is_visible("text=Остались вопросы?Оставьте заявкуна консультацию")
    
    def is_specialists_section_visible(self):
        """Проверка что раздел 'Специалисты' видима после перехода"""
        return self.page.is_visible("text=Наш стек")
    
    # === МЕТОДЫ ПРОВЕРКИ АТРИБУТОВ ССЫЛОК ===
    
    def get_telegram_support_href(self):
        """Получение href атрибута ссылки 'ТГ поддержка'"""
        return self.page.get_attribute(self.telegram_support_link, "href")
    
    def get_telegram_href(self):
        """Получение href атрибута ссылки 'Telegram'"""
        return self.page.get_attribute(self.telegram_link, "href")
    
    def get_email_href(self):
        """Получение href атрибута email ссылки"""
        return self.page.get_attribute(self.email_link, "href")
    
    def get_privacy_href(self):
        """Получение href атрибута ссылки 'Политика конфиденциальности'"""
        return self.page.get_attribute(self.privacy_link_1, "href")
    
    