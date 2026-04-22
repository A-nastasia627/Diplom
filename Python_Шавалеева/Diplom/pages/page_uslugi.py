from components.header import Header
from controls.pagination import Pagination
from pages.base_page import BasePage


class PageUslugi(BasePage):
    ''' Страница Услуги клиники Alimma '''

    def __init__(self, page):
        url = "https://alimma-ufa.ru/uslugi/"
        super().__init__(page, url)
        self.header = Header(page)
        pagination_wrapper = self.page.locator("div.pagination-area").first
        self.pagination = Pagination(page, pagination_wrapper)

    def get_uslugi(self):
        return self.page.locator(".rtin-item")

    def get_uslugi_all(self) -> list:
        return self.get_uslugi().all()

    def get_name_uslugi(self) -> list:
        items = self.get_uslugi_all()
        names = []
        for item in items:
            title_elem = item.locator("h3.item-title a")
            if title_elem.count() > 0:
                names.append(title_elem.first.inner_text().strip())
        return names

    def count_uslugi(self) -> int:
        return len(self.get_name_uslugi())

    def click_number(self, number: int):
        self.pagination.go_to_page(number)
