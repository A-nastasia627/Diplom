from pages.base_page import BasePage


class PriceUslug(BasePage):
    ''' Страница Цен клиники Alimma '''

    def __init__(self, page):
        url = "https://alimma-ufa.ru/price/"
        super().__init__(page, url)

    def click_section(self, section_name: str):
        section = self.page.locator(f'div.elementor-tab-title:has(a.elementor-toggle-title:has-text("{section_name}"))')
        section.scroll_into_view_if_needed()
        section.wait_for(state='visible', timeout=5000)
        section.click()

    def get_table(self):
        table = self.page.locator('div.elementor-tab-content.elementor-active table.tbl')
        return table.is_visible()

    def get_table_code(self, code: str):
        return self.page.locator(f'table.tbl tr:has(td.tbl-kod:has-text("{code}"))')

    def get_table_name_uslugi(self, name: str):
        return self.page.locator(f'table.tbl tr:has(td.tbl-naz:has-text("{name}"))')

    def get_table_price(self, price: str):
        return self.page.locator(f'table.tbl tr:has(td.tbl-cena:has-text("{price}"))')

    def get_price_by_code(self, code: str):
        row = self.get_table_code(code)
        return row.locator("td.tbl-cena")

    def get_price_by_name(self, name: str):
        row = self.get_table_name_uslugi(name)
        return row.locator("td.tbl-cena")
