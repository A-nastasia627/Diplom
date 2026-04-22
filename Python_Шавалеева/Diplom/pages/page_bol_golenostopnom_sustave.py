from pages.base_page import BasePage


class RevmatologGolenostop(BasePage):
    ''' Страница Лечение боли в голеностопном сутставе в Уфе'''
    def __init__(self, page):
        url = "https://alimma-ufa.ru/uslugi/travmatologiya/bol-v-golenostopnom-sustave/"
        super().__init__(page, url)
