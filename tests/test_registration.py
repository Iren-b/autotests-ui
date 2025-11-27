# Импортируем библиотеку pytest
import pytest
# Импорт Playwright для синхронного режима и проверки
from playwright.sync_api import sync_playwright, expect

@pytest.mark.regression  # Добавили маркировку regression
@pytest.mark.registration  # Добавили маркировку registration
def test_successful_registration():  # Создаем тестовую функцию
    # Запуск Playwright в синхронном режиме
    with sync_playwright() as playwright:
        # Запускаем Chromium браузер в обычном режиме (не headless)
        browser = playwright.chromium.launch(headless=False)
        # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
        context = browser.new_context()
        # Открываем новую страницу в рамках контекста
        page = context.new_page()

        # Переходим на страницу регистрации
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Находим поле "Email" и заполняем его
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill("user.name@gmail.com")

        # Находим поле "Username" и заполняем его
        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill("username")

        # Находим поле "Password" и заполняем его
        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill("password")

        # Находим кнопку "Registration" и кликаем на нее
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Проверяем, что отображается заголовок "Dashboard"
        dashboard_header = page.get_by_test_id('dashboard-toolbar-title-text')
        # Проверяем видимость элемента
        expect(dashboard_header).to_be_visible()
        # Проверяем текст
        expect(dashboard_header).to_have_text("Dashboard")

        # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

        page.wait_for_timeout(5000)