from components.base_component import BaseComponent
from playwright.sync_api import Page


class LogoHeader(BaseComponent):
    '''Логотип в Header'''
    def __init__(self, page: Page):
        self.logo = page.locator('a.dark-logo')
        super().__init__(page, self.logo)

    def click_logo(self):
        self.logo.click()
