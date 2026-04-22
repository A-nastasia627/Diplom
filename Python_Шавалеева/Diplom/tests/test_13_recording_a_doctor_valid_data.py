import allure
from playwright.sync_api import Page, expect
from components.cart_profile_doctor import CardProfileDoctor
from components.form_recording_a_doctor import FormRecording
from pages.page_nevrolog import PageNevrolog


@allure.title("Запись на приём на странице Неврология: отправка формы с валидными данными")
@allure.description("Форма записи отправляется, высвечивается сообщение: “Ваша заявка успешно отправлена! Наш "
                    "менеджер скоро с вами свяжется” ")
def test_recording_a_doctor_valid_data(page: Page):
    nevrolog_page = PageNevrolog(page, "Врач-невролог клиники Alimma")
    doctor_name = "Тихонова Ольга Ивановна"
    doctor_card = CardProfileDoctor(page, doctor_name)
    form = FormRecording(page)
    nevrolog_page.open()

    with allure.step("Пролистать до секции 'Врач-невролог клиники Alimma'"):
        nevrolog_page.scroll_to_section()

    with allure.step("Проверка отображения заголовка и карточки врача "):
        expect(nevrolog_page.section).to_have_text("Врач-невролог клиники Alimma")
        expect(doctor_card.wrapper).to_be_visible()

    with allure.step("Нажать кнопку “Записаться к врачу”, под анкетой врача"):
        doctor_card.click_recording_button()

    with allure.step("Проверка заголовка формы"):
        expect(form.title_form).to_have_text("Запись на прием")

    with allure.step("Ввести данные"):
        form.fill_input_name("Иван Кукаревич")
        form.fill_input_telephone("9177771122")
        form.fill_input_date("2026-04-29")
        form.fill_input_comment("Нужна консультация ревматолога на выбранную дату.")

    with allure.step("Нажать на кнопку- “Записаться”"):
        form.click_button_recording()

    with allure.step("Проверка уведомления об успешной записи"):
        form.get_success_message()
