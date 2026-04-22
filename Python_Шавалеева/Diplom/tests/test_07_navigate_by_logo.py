import allure
from playwright.sync_api import Page, expect
from pages.page_uslugi import PageUslugi


@allure.title("Переход на главную страницу через логотип")
@allure.description("Тестирование логотипа, преход на главную страницу сайта")
def test_navigate_by_logo(page: Page):
    uslugi_page = PageUslugi(page)
    uslugi_page.open()

    with allure.step("Кликнуть на логотип компании"):
        uslugi_page.header.click_logo()

    with allure.step("Проверка Url страницы"):
        expect(page).to_have_url("https://alimma-ufa.ru/")
