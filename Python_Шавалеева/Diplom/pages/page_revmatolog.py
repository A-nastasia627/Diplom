from pages.page_doctor_profile import DoctorProfile
from pages.base_page import BasePage
from components.cart_doctor import CartDoctor


class PageRevmatolog(BasePage):
    ''' Страница категории - Ревматолог'''
    def __init__(self, page):
        url = "https://alimma-ufa.ru/medilink_doctor_category/revmatolog/"
        super().__init__(page, url)

    def get_name_doctor(self, name_doctor: str):
        return CartDoctor(self.page, name_doctor)

    def click_about_me(self, name_doctor: str):
        doctor = self.get_name_doctor(name_doctor)
        doctor.click_button_about_me()
        return DoctorProfile(self.page)

    def click_about_me_doctor(self, doctor_name: str):
        return self.click_about_me(doctor_name)

    def get_doctor_cards_count(self) -> int:
        cards = self.page.locator(".team-box-layout2")
        return cards.count()

    def get_all_doctor_cards(self):
        return self.page.locator(".team-box-layout2")

    def get_doctor_cards(self):
        return self.page.locator(".team-box-layout2")
