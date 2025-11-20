# Импорт Playwright для синхронного режима и проверки
from playwright.sync_api import sync_playwright, expect

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    # Создаем новую страницу
    page = browser.new_page()

    # Переходим на страницу авторизации
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
