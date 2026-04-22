from components.base_component import BaseComponent
from controls.about_me import AboutMe


class CartDoctor(BaseComponent):
    ''' Карточка доктора'''
    def __init__(self, page, doctor_name):
        self.doctor_name = doctor_name
        super().__init__(page, page.locator(f".team-box-layout2:has(.item-title a:has-text('{doctor_name}'))"))

    def get_button_about_me(self):
        return AboutMe(self.page, self.wrapper)

    def click_button_about_me(self):
        self.get_button_about_me().wrapper.click()
