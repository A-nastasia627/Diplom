from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class Pagination(BaseControl):
    ''' Кнопки Пагинации '''

    def __init__(self, page: Page,
                 wrapper: Locator):
        super().__init__(page, wrapper)

    def get_button_prev(self):
        return self.wrapper.locator("li a:has(i.fa-angle-double-left)")

    def click_button_prev(self):
        self.get_button_prev().click()

    def get_button_next(self):
        return self.wrapper.locator("li a:has(i.fa-angle-double-right)")

    def click_button_next(self):
        self.get_button_next().click()

    def get_actual_number(self) -> int:
        active_li = self.wrapper.locator("li.active a")
        if active_li.count() > 0:
            return int(active_li.first.inner_text().strip())
        return 1

    def go_to_page(self, page_number: int):
        link = self.wrapper.locator(f"li a:has-text('{page_number}')")
        if link.count() > 0:
            link.first.click()
        else:
            raise Exception(f"Ссылка наc страницу {page_number} не найдена")

    def get_active_button(self):
        return self.wrapper.locator("li.active a")
