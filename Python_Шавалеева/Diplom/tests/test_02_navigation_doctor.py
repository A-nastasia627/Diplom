import allure
from playwright.sync_api import Page, expect
from pages.main_page import MainPage
from pages.page_specialists import PageSpecialist


@allure.title("Навигация по меню, переход в раздел- Врачи.")
@allure.description("Тестирование главного меню, проверки URL, наличие заголовка на странице")
def test_navigation_doctor(page: Page):
    main_page = MainPage(page)
    main_page.open()

    with allure.step("Кликнуть на пункт меню 'Врачи'"):
        header = main_page.get_header()
        header.click_menu_link("Врачи")

    with allure.step("Проверка Url адреса страницы"):
        speczialisty = PageSpecialist(page)
        expect(page).to_have_url(speczialisty.url)

    with allure.step("Проверка заголовка страницы'"):
        speczialisty.check_title_h1("Специалисты клиники Alimma")
