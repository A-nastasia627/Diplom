from pages.base_page import BasePage


class PageSpecialist(BasePage):
    ''' Страница Специалисы клиники Alimma '''
    def __init__(self, page):
        url = "https://alimma-ufa.ru/speczialisty-kliniki/"
        super().__init__(page, url)

    def get_doctors_list(self):
        return self.page.locator('.doctor-item').all()

    def get_doctor_count(self):
        return self.page.locator('.doctor-item').count()
