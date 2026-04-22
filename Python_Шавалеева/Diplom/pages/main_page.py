from playwright.sync_api import expect
from components.carousel_uslugi import CarouselUslugi
from components.header import Header
from pages.base_page import BasePage
from controls.messenger_link import MessengerLink


class MainPage(BasePage):
    ''' Главная страница '''
    def __init__(self, page):
        self.carusel = CarouselUslugi
        self.url = "https://alimma-ufa.ru/"
        super().__init__(page, self.url)
        self.header = Header(page)
        self.messenger_link = MessengerLink(page, page.locator("body"))

    def open_main_page(self):
        self.page.goto(self.url)

    def get_header(self):
        return Header(self.page)

    def is_logo_visible(self) -> bool:
        header = self.get_header()
        return header.logo.wrapper.is_visible()
    
    def click_link_messenger(self):
        self.messenger_link.click_link_messenger()

    def check_title_h2(self, title: str):
        expect(self.page.get_by_role("heading", name=title, level=2)).to_have_text(title)
