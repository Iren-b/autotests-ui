# Импортируем библиотеку pytest
import pytest
# Импорт Playwright для синхронного режима и проверки
from playwright.sync_api import sync_playwright, expect, Page

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):

        chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверяем, что отображается заголовок "Courses"
        courses_header = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        # Проверяем видимость заголовка "Courses"
        expect(courses_header).to_be_visible()
        # Проверяем текст заголовка "Courses"
        expect(courses_header).to_have_text("Courses")

        # Проверяем, что отображается иконка пустого блока
        courses_list_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        # Проверяем видимость иконки пустого блока
        expect(courses_list_icon).to_be_visible()

        # Проверяем, что отображается блок "There is no results"
        courses_list_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        # Проверяем видимость блока "There is no results"
        expect(courses_list_title).to_be_visible()
        # Проверяем текст блока "There is no results"
        expect(courses_list_title).to_have_text("There is no results")

        # Проверяем, что отображается блок "Results from the load test pipeline will be displayed here"
        courses_list_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        # Проверяем видимость блока "Results from the load test..."
        expect(courses_list_description).to_be_visible()
        # Проверяем текст блока "Results from the load test..."
        expect(courses_list_description).to_have_text("Results from the load test pipeline will be displayed here")

