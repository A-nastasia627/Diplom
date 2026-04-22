import allure
from playwright.sync_api import Page, expect
from pages.main_page import MainPage
from pages.page_price_uslug import PriceUslug


@allure.title("Страница цен, отображение таблицы Ревматолог")
@allure.description("Тестирование страницы Цены, отображение таблицы раздел Ревматолог")
def test_prices_for_services(page: Page):
    main_page = MainPage(page)
    price = PriceUslug(page)
    main_page.open()

    with allure.step("Кликнуть на пункт меню 'Цены'"):
        header = main_page.get_header()
        header.click_menu_link("Цены")

    with allure.step("Проверка Url страницы "):
        expect(page).to_have_url(price.url)

    with allure.step("Проверка заголовка страницы "):
        price.check_title_h1("Цены на медицинские услуги")

    with allure.step("Кликнуть по разделу 'Ревматолог'"):
        page.wait_for_timeout(2000)
        price.click_section("Ревматолог")
        assert price.get_table(), "Таблица с ценами не видима"

    with allure.step("Проверка наличия услуги по коду "):
        data_code = price.get_table_code("В01.040.001")
        expect(data_code).to_be_visible()

    with allure.step("Проверка наличия услуги по названию "):
        data_name = price.get_table_name_uslugi(
            "Первичный прием (осмотр, консультация) врача ревматолога 1 категории, с выдачей заключения на руки")
        expect(data_name).to_be_visible()

    with allure.step("Проверка цены услуги с определенным кодом "):
        price_cell = price.get_price_by_code("В01.040.001")
        expect(price_cell).to_have_text("3 300")
