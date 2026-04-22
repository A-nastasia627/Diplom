from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class CarouselArrows(BaseControl):
    ''' Стрелки вперед, назад в карусели Услуги '''

    def __init__(self, page: Page,
                 wrapper: Locator):
        super().__init__(page, wrapper)
        self.button_prev = wrapper.locator('.owl-prev')
        self.button_next = wrapper.locator('.owl-next')

    def click_prev(self):
        self.button_prev.click()

    def click_next(self):
        self.button_next.click()
