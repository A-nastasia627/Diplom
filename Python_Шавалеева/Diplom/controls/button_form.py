from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class ButtonForm(BaseControl):
    ''' Кнопки "Записаться к врачу " и "Закрытие" в форме записи на прием'''
    def __init__(self, page: Page,
                 wrapper: Locator):
        super().__init__(page, wrapper)

    def get_button_recording(self):
        return self.wrapper.locator('button.g4_send_cf7_form')

    def click_button_recording(self):
        self.get_button_recording().click()

    def get_button_close(self):
        return self.wrapper.locator(".pum-close")

    def click_close(self):
        self.get_button_close().click()
