# Импортируем библиотеку pytest
import pytest
# Импорт Playwright для синхронного режима и проверки
from playwright.sync_api import sync_playwright, expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
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

        # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверяем, что отображается заголовок "Courses"
        courses_header = page.get_by_test_id('courses-list-toolbar-title-text')
        # Проверяем видимость заголовка "Courses"
        expect(courses_header).to_be_visible()
        # Проверяем текст заголовка "Courses"
        expect(courses_header).to_have_text("Courses")

        # Проверяем, что отображается иконка пустого блока
        courses_list_icon = page.get_by_test_id('courses-list-empty-view-icon')
        # Проверяем видимость иконки пустого блока
        expect(courses_list_icon).to_be_visible()

        # Проверяем, что отображается блок "There is no results"
        courses_list_title = page.get_by_test_id('courses-list-empty-view-title-text')
        # Проверяем видимость блока "There is no results"
        expect(courses_list_title).to_be_visible()
        # Проверяем текст блока "There is no results"
        expect(courses_list_title).to_have_text("There is no results")

        # Проверяем, что отображается блок "Results from the load test pipeline will be displayed here"
        courses_list_description = page.get_by_test_id('courses-list-empty-view-description-text')
        # Проверяем видимость блока "Results from the load test..."
        expect(courses_list_description).to_be_visible()
        # Проверяем текст блока "Results from the load test..."
        expect(courses_list_description).to_have_text("Results from the load test pipeline will be displayed here")

