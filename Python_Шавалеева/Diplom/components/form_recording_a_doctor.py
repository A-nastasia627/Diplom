from playwright.sync_api import Page, Locator, expect
from components.base_component import BaseComponent
from controls.button_form import ButtonForm
from controls.input_form import InputForm


class FormRecording(BaseComponent):
    ''' Форма записи на прием'''
    def __init__(self, page: Page):
        wrapper = page.locator("#popmake-3802")
        super().__init__(page, wrapper)
        self.title_form = self.wrapper.locator(".pum-title")
        self.success_message = self.wrapper.locator(".form_success")
        self.name_input = InputForm(self.wrapper.locator('input[name="your-name"]'))
        self.phone_input = InputForm(self.wrapper.locator('input[name="tel-214"]'))
        self.date_input = InputForm(self.wrapper.locator('input[name="date-464"]'))
        self.comment_input = InputForm(self.wrapper.locator('textarea[name="textarea-835"]'))
        self.submit_button = ButtonForm(page, self.wrapper)

    def fill_input_name(self, name: str):
        self.name_input.fill(name)

    def fill_input_telephone(self, phone: str):
        self.phone_input.fill(phone)

    def fill_input_date(self, date: str):
        self.date_input.fill(date)

    def fill_input_comment(self, text: str) :
        self.comment_input.fill(text)

    def click_button_recording(self):
        self.submit_button.click_button_recording()

    def get_name_error(self) -> Locator:
        return self.name_input.get_error()

    def get_telephone_error(self) -> Locator:
        return self.phone_input.get_error()

    def get_date_error(self) -> Locator:
        return self.date_input.get_error()

    def check_title(self, title: str):
        expect(self.title_form).to_have_text(title)

    def get_success_message(self):
        expect(self.success_message.locator("p span")).to_have_text("Ваша заявка успешно отправлена!")
        expect(self.success_message.locator("p").last).to_have_text("Наш менеджер скоро с вами свяжется")

    def get_name_label(self) -> Locator:
        return self.wrapper.locator('label.form_name')

    def get_phone_label(self) -> Locator:
        return self.wrapper.locator('label.form_phone')

    def get_date_label(self) -> Locator:
        return self.wrapper.locator('label.form_date')
