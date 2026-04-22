import allure
from playwright.sync_api import Page, expect
from components.cart_profile_doctor import CardProfileDoctor
from components.form_recording_a_doctor import FormRecording
from pages.page_nevrolog import PageNevrolog


@allure.title("Запись на приём на странице Неврология: отправка формы с неполными данными — проверка валидации")
@allure.description("Форма записи не отправляется, если обязательные поля (имя, телефон, дата) пусты")
def test_recording_a_doctor_incomplete_data(page: Page):
    nevrolog_page = PageNevrolog(page, "Врач-невролог клиники Alimma")
    doctor_name = "Тихонова Ольга Ивановна"
    doctor_card = CardProfileDoctor(page, doctor_name)
    form = FormRecording(page)
    nevrolog_page.open()

    with allure.step("Пролистать статью до секции- Врач-невролог клиники Alimma"):
        nevrolog_page.scroll_to_section()
        expect(nevrolog_page.section).to_have_text("Врач-невролог клиники Alimma")
        expect(doctor_card.wrapper).to_be_visible()
        page.wait_for_timeout(2000)

    with allure.step("Нажать кнопку “Записаться к врачу”, под анкетой врача"):
        doctor_card.click_recording_button()
        expect(form.title_form).to_have_text("Запись на прием")
        page.wait_for_timeout(2000)

    with allure.step("Заполнить форму не полными данными"):
        expect(form.title_form).to_be_visible()
        form.fill_input_name(",Mbuygt76")
        form.fill_input_telephone("")
        form.fill_input_date("")
        form.fill_input_comment("")

    with allure.step("Нажать кнопку “Записаться”, под анкетой врача"):
        form.click_button_recording()

    with allure.step("Проверка уведомлений о необходимости заполнить данные номер тлефона"):
        expect(form.get_telephone_error()).to_have_text("Это поле является обязательным.")

    with allure.step("Проверка уведомлений о необходимости заполнить данные даты приема"):
        expect(form.get_date_error()).to_have_text("Это поле является обязательным.")
