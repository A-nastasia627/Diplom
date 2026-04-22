from components.base_component import BaseComponent


class CardProfileDoctor(BaseComponent):
    ''' Карточка профиля доктора с данными'''
    def __init__(self, page, doctor_name):
        self.doctor_name = doctor_name
        super().__init__(page, page.locator(f".doctor-card:has(.doctor-card__title:has-text('{doctor_name}'))"))

    def get_recording_button_by_name(self):
        return self.wrapper.locator("a:has-text('Записаться к врачу')")

    def click_recording_button(self):
        self.get_recording_button_by_name().click()