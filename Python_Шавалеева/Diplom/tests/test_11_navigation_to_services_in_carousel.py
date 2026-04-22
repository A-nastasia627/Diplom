import allure
from playwright.sync_api import Page, expect
from pages.main_page import MainPage
from components.carousel_uslugi import CarouselUslugi
from pages.page_bol_golenostopnom_sustave import RevmatologGolenostop


@allure.title("Карусель услуги, навигация в раздел")
@allure.description("Тестирование навигации в услуги через карусель на главной странице сайта ")
def test_navigation_to_services_in_carousel(page: Page):
    main_page = MainPage(page)
    carusel = CarouselUslugi(page)
    main_page.open()

    with allure.step("На галавной странице сайта пролистать до карусели 'Услуги' "):
        carusel.carusel.scroll_into_view_if_needed()
        expect(carusel.carusel).to_be_visible()

    with allure.step("Проверка заголовка раздела "):
        main_page.check_title_h2("Услуги")

    with allure.step("Нажать на стрелку в правой стороне до появления нужной услуги:'Лечение боли в голеностопном "
                     "суставе'"):
        get_title = "Лечение боли в голеностопном суставе"
        found = carusel.scroll_to_item_by_title(get_title)

    with allure.step("Проверка что отобразилась нужная услуга"):
        assert found, f"Карточка с названием '{get_title}' не найдена"

    with allure.step("Нажать на карточку – “Лечение боли в голеностопном суставе"):
        carusel.click_item_by_title(get_title)

    with allure.step("Проверка Url адреса, перехода на новую страницу"):
        expected_url = RevmatologGolenostop(page).url
        expect(page).to_have_url(expected_url)
