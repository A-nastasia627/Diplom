import allure
from playwright.sync_api import Page, expect
from components.cart_profile_doctor import CardProfileDoctor
from components.form_recording_a_doctor import FormRecording
from pages.page_nevrolog import PageNevrolog


@allure.title("Запись на приём на странице Неврология: отправка формы с невалидными данными")
@allure.description("Форма записи не отправляется, появляются сообщения о некорректных данных")
def test_recording_a_doctor_invalid_data(page: Page):
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

    with allure.step("Ввести данные"):
        form.fill_input_name("Зу12Ru")
        form.fill_input_telephone("00110011001")
        form.fill_input_date("11111-11-11")
        form.fill_input_comment("You need записаться a rheumatologist %& прием 275760 dates.")

    with allure.step("Нажать на кнопку “Записаться”"):
        form.click_button_recording()

    with allure.step("Проверка уведомлений о некорректно введенных данных фамилии и имени "):
        expect(form.get_name_error()).to_have_text("Введены некорректные данные")

    with allure.step("Проверка уведомлений о некорректно введенных данных телефонного номера"):
        expect(form.get_telephone_error()).to_have_text("Введён некорректный телефонный номер")

    with allure.step("Проверка уведомлений о некорректно введенных данных даты записи на прием "):
        expect(form.get_date_error()).to_have_text("Введена некорректная дата")
