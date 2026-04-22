import allure
from playwright.sync_api import Page, expect
from pages.main_page import MainPage
from pages.page_uslugi import PageUslugi


@allure.title("Пагинация кнопки Вперед- Next")
@allure.description("Активность кнопки Next в пагинации, смена URL, изменение цвета активной кнопки, изменение "
                    "контента на странице")
def test_pagination_next(page: Page):
    main_page = MainPage(page)
    uslugi = PageUslugi(page)
    main_page.open()

    with allure.step("Кликнуть на пункт меню 'Услуги'"):
        header = main_page.get_header()
        header.click_menu_link("Услуги")

    with allure.step("Проверка Url страницы Услуг"):
        expect(page).to_have_url(uslugi.url)

    with allure.step("Проверика заголовок страницы H1"):
        uslugi.check_title_h1("Услуги")

    with allure.step("Проверка отображения услуг на странице 1"):
        names_page1 = uslugi.get_name_uslugi()

    with allure.step("Проверка цвета активной кнопки пагинации (страница 1)"):
        active_button = uslugi.pagination.get_active_button()
        expect(active_button).to_have_css("background-color", "rgb(0, 162, 156)"), f"Цвет активной кнопки не: {active_button}"

    with allure.step("Нажать на кнопку Next"):
        page.wait_for_timeout(2000)
        uslugi.pagination.click_button_next()

    with allure.step("Проверка видимость кнопки Prev"):
        expect(uslugi.pagination.get_button_prev()).to_be_visible()

    with allure.step("Проверка URL после перехода на страницу 2"):
        expect(page).to_have_url("https://alimma-ufa.ru/uslugi/page/2/")

    with allure.step("Проверка номер активной кнопки в пагинации"):
        assert uslugi.pagination.get_actual_number() == 2, "Активная страница не 2"

    with allure.step("Проверка изменения услуг на странице 2"):
        names_page2 = uslugi.get_name_uslugi()
        assert names_page1 != names_page2, "Списки услуг на первой и второй странице одинаковы"

        active_button_page2 = uslugi.pagination.get_active_button()
        expect(active_button_page2).to_have_css("background-color", "rgb(0, 162, 156)"), f"Цвет активной кнопки на странице 2 не: {active_button}"

    with allure.step("Проверка отображения кнопки 'Previous'"):
        expect(uslugi.pagination.get_button_prev()).to_be_visible()
