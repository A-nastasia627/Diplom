import allure
from playwright.sync_api import Page, expect
from pages.main_page import MainPage


@allure.title("Загрузка главной страницы сайта Alimma.")
@allure.description("Главная страница успешно загружается, в шапке сайта логотип компании.")
def test_open_maim_page(page: Page):
    main_page = MainPage(page)

    with allure.step("Открытие главной страницы сайта."):
        main_page.open()
        page.wait_for_timeout(2000)

    with allure.step("Проверка URL и логотипа главной страницы"):
        expect(page).to_have_url("https://alimma-ufa.ru/")

        header = main_page.get_header()
        expect(header.logo.wrapper).to_be_visible()
