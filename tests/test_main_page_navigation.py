import allure
import pytest
from pages.main_page import MainPage

class TestMainPageNavigation:
    """
    Метод содержит тесты для всех основных элементов навигации и ссылок
    """
    
    @allure.title("Проверка перехода на главную страницу")
    def test_main_link(self, main_page: MainPage):
        with allure.step("Кликаем на иконку главной страницы"):
            main_page.click_main()
        
        with allure.step("Проверяем URL"):
            assert "#main" in main_page.get_url()
        
        with allure.step("Проверяем что главная страница видна"):
            assert main_page.is_main()
    
    @allure.title("Проверка перехода в раздел 'О нас'")
    def test_about_link(self, main_page: MainPage):
        with allure.step("Кликаем на ссылку 'О нас'"):
            main_page.click_about_link()
        
        with allure.step("Проверяем URL"):
            assert "#about" in main_page.get_url()
        
        with allure.step("Проверяем что раздел 'О нас' видим"):
            assert main_page.is_about_section_visible()
    
    @allure.title("Проверка перехода в раздел 'Услуги'")
    def test_services_link(self, main_page: MainPage):
        with allure.step("Кликаем на ссылку 'Услуги'"):
            main_page.click_services_link()
        
        with allure.step("Проверяем URL"):
            assert "#moreinfo" in main_page.get_url()
        
        with allure.step("Проверяем что раздел 'Услуги' видим"):
            assert main_page.is_services_section_visible()
        
    @allure.title("Проверка перехода в раздел 'Проекты'")
    def test_projects_link(self, main_page: MainPage):
        with allure.step("Кликаем на ссылку 'Проекты'"):
            main_page.click_projects_link()
    
        with allure.step("Проверяем URL"):
            assert "#cases" in main_page.get_url()
    
        with allure.step("Проверяем что раздел 'Проекты' видим"):
            assert main_page.is_projects_section_visible()
            
    @allure.title("Проверка перехода в раздел 'Отзывы'")
    def test_reviews_link(self, main_page: MainPage):
        with allure.step("Кликаем на ссылку 'Отзывы'"):
            main_page.click_reviews_link()
            
        with allure.step("Проверяем URL"):
            assert "#Reviews" in main_page.get_url()
            
        with allure.step("Проверяем что раздел 'Отзывы' видим"):
            assert main_page.is_reviews_section_visible()
            
    @allure.title("Проверка перехода в раздел 'Контакты'")
    def test_contacts_link(self, main_page: MainPage):
        with allure.step("Кликаем на ссылку 'Контакты'"):
            main_page.click_contacts_link()
            
        with allure.step("Проверяем URL"):
            assert "#contacts" in main_page.get_url()
            
        with allure.step("Проверяем что раздел 'Контакты' видим"):
            assert main_page.is_contacts_section_visible()
            
    @allure.title("Проверка перехода в раздел 'Специалисты'")
    def test_specialists_link(self, main_page: MainPage):
        with allure.step("Кликаем на ссылку 'Выбрать специалиста'"):
            main_page.click_specialists_link()
            
        with allure.step("Проверяем URL"):
            assert "#specialists" in main_page.get_url()
            
        with allure.step("Проверяем что раздел 'Специалисты' видим"):
            assert main_page.is_specialists_section_visible()
            
    @allure.title("Проверка перехода в раздел 'Услуги' с помощью кнопки 'Подробнее'")
    def test_details_button(self, main_page: MainPage):
        with allure.step("Кликаем на ссылку 'Подробнее'"):
            main_page.click_details_button()
        
        with allure.step("Проверяем URL"):
            assert "#moreinfo" in main_page.get_url()
        
        with allure.step("Проверяем что раздел 'Услуги' видим"):
            assert main_page.is_services_section_visible()
            
    @allure.title("Проверка перехода в раздел 'Контакты' с помощью кнопки 'Оставить заявку на сотрудничество'")
    def test_cooperation_button(self, main_page: MainPage):
        with allure.step("Кликаем на ссылку 'Оставить заявку на сотрудничество'"):
            main_page.click_cooperation_button()
            
        with allure.step("Проверяем URL"):
            assert "#contacts" in main_page.get_url()
            
        with allure.step("Проверяем что раздел 'Контакты' видим"):
            assert main_page.is_contacts_section_visible()
            
    @allure.title("Проверка ссылки 'ТГ поддержка'")
    def test_telegram_support_link(self, main_page: MainPage):
        with allure.step("Проверяем адрес ссылки"):
            href = main_page.get_telegram_support_href()
            assert href == "https://t.me/assistant_em"
    
        with allure.step("Кликаем и проверяем переход"):
            main_page.click_telegram_support_link()
            main_page.page.wait_for_timeout(2000)

    @allure.title("Проверка ссылки 'Telegram'")
    def test_telegram_link(self, main_page: MainPage):
        with allure.step("Проверяем адрес ссылки"):
            href = main_page.get_telegram_href()
            assert href == "https://t.me/krasnikova_d"
        
        with allure.step("Кликаем и проверяем переход"):
            main_page.click_telegram_link()
            main_page.page.wait_for_timeout(2000)
 
    @allure.title("Проверка email ссылки")
    def test_email_link(self, main_page: MainPage):
        with allure.step("Проверяем href email"):
            href = main_page.get_email_href()
            assert href == "mailto:dariia.krasnikova@effectivemobile.ru"

    @allure.title("Проверка ссылки 'Политика конфиденциальности' в разделе 'Контакты'")
    def test_privacy_link_1(self, main_page: MainPage):
        with allure.step("Проверяем адрес политики конфиденциальности"):
            href = main_page.get_privacy_href()
            assert href == "https://effective-mobile.ru/privacy"
            
    @allure.title("Проверка ссылки 'Политика конфиденциальности' в Footer")
    def test_privacy_link_2(self, main_page: MainPage):
        with allure.step("Проверяем адрес политики конфиденциальности"):
            href = main_page.get_privacy_href()
            assert href == "https://effective-mobile.ru/privacy"
    