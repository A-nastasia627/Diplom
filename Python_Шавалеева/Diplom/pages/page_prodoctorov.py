import re
from playwright.sync_api import expect
from pages.base_page import BasePage


class PageProdoctorov(BasePage):
    ''' Страница с отзывами на Prodoctorov '''
    def __init__(self, page):
        super().__init__(page, url='')

    def check_is_prodoctorov(self):
        expect(self.page).to_have_url(re.compile(r"https?://(www\.)?prodoctorov\.ru/.*"))
