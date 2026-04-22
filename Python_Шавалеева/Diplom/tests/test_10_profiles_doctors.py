import allure
from playwright.sync_api import Page, expect
from pages.page_revmatolog import PageRevmatolog


@allure.title("Открытие профиля доктора на странице Ремватолог")
@allure.description("Отображение данных о враче: описание обо мне, информацию об учебе.")
def test_profile_doctor(page: Page):
    page_revmatolog = PageRevmatolog(page)
    page_revmatolog.open()

    with allure.step("Кликнуть - Обо мне, врача Каримова Лилия."):
        profile = page_revmatolog.click_about_me_doctor("Каримова Лилия Ильсуровна")

    with allure.step("Проверка Url страницы "):
        expect(page).to_have_url("https://alimma-ufa.ru/doctors/karimova-liliya-ilsurovna/")

    with allure.step("Отображение заголовка страницы"):
        profile.check_title_h1("Каримова Лилия Ильсуровна")

    with allure.step("Отображение заголовка анкеты Обо Мне"):
        expect(profile.get_title_about_me()).to_be_visible()

    with allure.step("Отображение заголовка таблицы Дипломы И Сертификаты"):
        expect(profile.get_title_diplom()).to_be_visible()
        table = profile.diplom_table()

    with allure.step("Проверка отображения данных в таблице: год, степерь, университет"):
        expect(profile.diplom_table_year(0)).to_contain_text("24.06.2019")
        expect(profile.diplom_table_stepen(0)).to_contain_text("Диплом специалиста")
        expect(profile.diplom_table_university(0)).to_contain_text("Башкирский государственный медицинский университет")

    with allure.step("Проверка отображения кнопки 'Запиcаться на прием'"):
        expect(profile.get_appointment_button()).to_be_visible()
