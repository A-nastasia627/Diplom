from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class AboutMe(BaseControl):
    """Кнопка Обо мне"""
    def __init__(self, page: Page,
                 paren_wrapper: Locator,
                 self_wrapper_path='a.item-btn:has-text("Обо мне")'):
        super().__init__(page, paren_wrapper.locator(self_wrapper_path))
