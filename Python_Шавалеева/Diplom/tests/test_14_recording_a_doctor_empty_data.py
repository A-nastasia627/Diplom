import allure
from playwright.sync_api import Page, expect
from components.cart_profile_doctor import CardProfileDoctor
from components.form_recording_a_doctor import FormRecording
from pages.page_nevrolog import PageNevrolog


@allure.title("Запись на приём на странице Неврология: отправка формы с незополненными данными")
@allure.description("Форма записи не отправляется, под полями ввода появляются уведомления: “Это поле является "
                    "обязательным”")
def test_recording_a_doctor_empty_data(page: Page):
    nevrolog_page = PageNevrolog(page, "Врач-невролог клиники Alimma")
    doctor_name = "Тихонова Ольга Ивановна"
    doctor_card = CardProfileDoctor(page, doctor_name)
    form = FormRecording(page)
    nevrolog_page.open()

    with allure.step("Пролистать статью до секции- Врач-невролог клиники Alimma"):
        nevrolog_page.scroll_to_section()

    with allure.step("Проверка отображения заголовка и карточки врача "):
        expect(nevrolog_page.section).to_have_text("Врач-невролог клиники Alimma")
        expect(doctor_card.wrapper).to_be_visible()

    with allure.step("Нажать кнопку “Запись на прием”, под анкетой врача"):
        doctor_card.click_recording_button()

    with allure.step("Проверка заголовка формы"):
        expect(form.title_form).to_have_text("Запись на прием")

    with allure.step("Не вводить данные, нажать на кнопку 'Записаться'"):
        form.fill_input_name("")
        form.fill_input_telephone("")
        form.fill_input_date("")
        form.fill_input_comment("")
        page.wait_for_timeout(2000)
        form.click_button_recording()

    with allure.step("Проверка уведомлений о необходимости заполнить данные имени и фамилии"):
        expect(form.get_name_error()).to_have_text("Это поле является обязательным.")

    with allure.step("Проверка уведомлений о необходимости заполнить данные телефонного номера"):
        expect(form.get_telephone_error()).to_have_text("Это поле является обязательным.")

    with allure.step("Проверка уведомлений о необходимости заполнить данные записи на прием"):
        expect(form.get_date_error()).to_have_text("Это поле является обязательным.")
