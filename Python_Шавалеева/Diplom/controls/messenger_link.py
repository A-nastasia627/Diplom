from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class MessengerLink(BaseControl):
    ''' Ссылка-иконка для открытия чата'''

    def __init__(self, page: Page,
                 wrapper: Locator):
        super().__init__(page, wrapper)

    def get_link_messenger(self):
        return self.wrapper.locator("a.mvvwo_btn")

    def click_link_messenger(self):
        self.get_link_messenger().click()
