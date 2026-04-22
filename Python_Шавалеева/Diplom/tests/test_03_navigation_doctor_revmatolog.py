import allure
from playwright.sync_api import Page, expect
from pages.main_page import MainPage
from pages.page_revmatolog import PageRevmatolog


@allure.title("Навигация через выпадающее подменю, переход к разделу Врачи- Ревматолог")
@allure.description("Переход на страницу через подменю, проверка изменения URL, заголовка, отображение карточки врача")
def test_navigation_doctor_revmatolog(page: Page):
    main_page = MainPage(page)
    main_page.open()

    with allure.step("Навести курсор на пункт меню 'Врачи'"):
        header = main_page.get_header()
        header.hover_menu("Врачи")

    with allure.step("Кликнуть на подпункт меню 'Ревматолог'"):
        header.click_submenu("Врачи", "Ревматолог")
        revmatolog = PageRevmatolog(page)

    with allure.step("Проверка Url адреса страницы и заголовка"):
        expect(page).to_have_url(revmatolog.url)
        revmatolog.check_title_h1("Ревматолог")

    with allure.step("Проверка отображения карточек докторов"):
        expect(revmatolog.get_doctor_cards().first).to_be_visible()
