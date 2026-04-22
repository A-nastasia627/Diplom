from playwright.sync_api import Page
from pages.base_page import BasePage


class DoctorProfile(BasePage):
    def __init__(self, page: Page, url=None):
        super().__init__(page, url)

    def get_title_about_me(self):
        return self.page.locator("h3.section-title:has-text('Обо Мне:')")

    def get_text_about_me(self):
        return self.page.locator("div.single-item p[align='justify']")

    def get_title_diplom(self):
        return self.page.locator("h3.section-title:has-text('Дипломы И Сертификаты:')")

    def diplom_table(self):
        return self.page.locator("table.table tbody tr")

    def diplom_table_year(self, index: int = 0):
        return self.page.locator(f"table.table tbody tr:nth-child({index + 1}) td:nth-child(1)")

    def diplom_table_stepen(self, index: int = 0):
        return self.page.locator(f"table.table tbody tr:nth-child({index + 1}) td:nth-child(2)")

    def diplom_table_university(self, index: int = 0):
        return self.page.locator(f"table.table tbody tr:nth-child({index + 1}) td:nth-child(3)")

    def get_appointment_button(self):
        return self.page.locator("a.knopka:has-text('Записаться на прием')")
