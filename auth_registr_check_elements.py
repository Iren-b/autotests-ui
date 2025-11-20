# Импорт Playwright для синхронного режима и проверки
from playwright.sync_api import sync_playwright, expect

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    # Создаем новую страницу
    page = browser.new_page()

    # Переходим на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Находим поле "Email"
    login_email_input = page.get_by_test_id('login-form-email-input').locator('input')
    expect(login_email_input).to_be_visible()

    # Находим поле "Password"
    login_password_input = page.get_by_test_id('login-form-password-input').locator('input')
    expect(login_password_input).to_be_visible()

    # Находим кнопку "Login"
    login_button = page.get_by_test_id('login-page-login-button')
    expect(login_button).to_be_visible()

    # Находим ссылку "Registration" и кликаем на неё
    registration_link = page.get_by_test_id("login-page-registration-link")
    registration_link.click()

    # Находим поле "Email"
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(registration_email_input).to_be_visible()

    # Находим поле "Password"
    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(registration_password_input).to_be_visible()

    # Находим кнопку "Registration"
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_visible()

    # Пауза на 5 секунд, чтобы увидеть результат
    page.wait_for_timeout(5000)













