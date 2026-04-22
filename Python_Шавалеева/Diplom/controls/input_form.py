from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class InputForm(BaseControl):
    """Инпут в форме записи на прием"""
    def __init__(self, locator: Locator):
        super().__init__(locator.page, locator)

    def fill(self, value: str):
        self.wrapper.fill(value)

    def get_value(self):
        return self.wrapper.input_value()

    def get_error(self):
        return self.wrapper.locator('.wpcf7-not-valid-tip')
