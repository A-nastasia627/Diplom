import allure
from playwright.sync_api import Page, expect
from pages.main_page import MainPage
from pages.page_uslugi import PageUslugi


@allure.title("Пагинация на странице Услуги, активность кнопки и смена контента")
@allure.description("Активность кнопки с цифрами в пагинации, смена URL, изменение цвета активной кнопки")
def test_pagination_count(page: Page):
    main_page = MainPage(page)
    main_page.open()

    with allure.step("Кликнуть на пункт меню 'Услуги'"):
        header = main_page.get_header()
        header.click_menu_link("Услуги")

    with allure.step("Проверка Url адреса страницы "):
        uslugi = PageUslugi(page)
        expect(page).to_have_url(uslugi.url)

    with allure.step("Проверка заголовок страницы H1"):
        uslugi.check_title_h1("Услуги")

    with allure.step("Проверка отображения услуг на странице 1"):
        expect(uslugi.get_uslugi().first).to_be_visible()
        # names_page1 = uslugi.get_name_uslugi()
        first_service_text_page1 = uslugi.get_uslugi().first.inner_text()

    with allure.step("Проверка отображения активной кнопки 1 в пагинации"):
        active_button = uslugi.pagination.get_active_button()
        expect(active_button).to_have_css("background-color", "rgb(0, 162, 156)")

    with allure.step("Кликнуть на цифру 2 в пагинации"):
        page.wait_for_timeout(2000)
        uslugi.click_number(2)

    with allure.step("Проверка Url адреса после перехода на страницу 2"):
        expect(page).to_have_url("https://alimma-ufa.ru/uslugi/page/2/")

    with allure.step("Проверка отображения активной кнопки 2"):
        active_button_after = uslugi.pagination.get_active_button()
        expect(active_button_after).to_have_css("background-color", "rgb(0, 162, 156)")

    with allure.step("Проверка изменения списка услуг на странице"):
        expect(uslugi.get_uslugi().first).to_be_visible()
        # names_page2 = uslugi.get_name_uslugi()
        # expect(names_page1).not_to_equal(names_page2)
        expect(uslugi.get_uslugi().first).not_to_have_text(first_service_text_page1)
