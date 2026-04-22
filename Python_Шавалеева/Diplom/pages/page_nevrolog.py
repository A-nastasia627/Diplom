from playwright.sync_api import expect
from components.cart_profile_doctor import CardProfileDoctor
from pages.base_page import BasePage


class PageNevrolog(BasePage):
    ''' Страница Неврологии'''
    def __init__(self, page, section_text):
        url = "https://alimma-ufa.ru/uslugi/nevrologiya/"
        super().__init__(page, url)
        self.section = page.locator(f"h3.elementor-heading-title:has-text('{section_text}')").first

    def get_section_title(self):
        return self.section.text_content()

    def scroll_to_section(self):
        self.section.scroll_into_view_if_needed()
        expect(self.section).to_be_visible()

    def get_doctor_card(self, doctor_name: str):
        return CardProfileDoctor(self.page, doctor_name)
