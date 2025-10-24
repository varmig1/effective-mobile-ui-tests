# UI Автотесты для effective-mobile.ru

Автоматизированные UI тесты для сайта effective-mobile.ru.

## 📋 Обзор проекта

Данный проект содержит UI тесты для навигации по главной странице effective-mobile.ru.

## 🛠️ Используемые технологии

- **Python 3.10** - язык программирования
- **Playwright** - автоматизация браузеров
- **pytest** - фреймворк для тестирования
- **Allure** - система отчетов
- **Docker** - контейнеризация

## 📁 Структура проекта

effective-mobile-ui-tests/
    pages/ # Классы Page Object
        base_page.py # Базовый класс страницы
        main_page.py # Класс главной страницы
    tests/ # Наборы тестов
        test_main_page_navigation.py
    conftest.py # Конфигурация pytest
    Dockerfile # Конфигурация Docker
    requirements.txt # Зависимости Python
    README.md # Документация проекта

## ⚡ Быстрый старт

### Предварительные требования
- Python 3.10 или выше
- Docker

### Локальная установка

1. **Клонируйте репозиторий**
    ```bash
    git clone https://github.com/yourusername/effective-mobile-ui-tests.git
    cd effective-mobile-ui-tests

2. **Настройте виртуальное окружение**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate

3. **Установите зависимости**
    ```bash
    pip install -r requirements.txt
    playwright install

4. **Запустите тесты**
    ```bash
    pytest tests/ -v

### Установка через Docker

**Соберите и запустите через Docker**
    ```bash
    docker build -t effective-mobile-tests .
    docker run effective-mobile-tests   

### Запуск тестов

1. **Базовый запуск тестов**
    ```bash
    # Запустить все тесты
    pytest tests/ -v

    # Запустить конкретный тест
    pytest tests/test_main_page_navigation.py::TestMainPageNavigation::test_about_link -v

2. **С отчетами Allure**
    ```bash
    # Сгенерировать результаты Allure
    pytest tests/ --alluredir=allure-results

    # Просмотреть отчет
    allure serve allure-results

### Автор
- **Иван Апасев**
- **GitHub** - varmig1