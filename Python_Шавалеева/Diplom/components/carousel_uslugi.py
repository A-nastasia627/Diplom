from playwright.sync_api import Page
from components.base_component import BaseComponent
from controls.carousel_arrows import CarouselArrows


class CarouselUslugi(BaseComponent):
    '''Карусель услуг на главной странице'''
    def __init__(self, page: Page):
        self.carusel = page.locator('#uslugi .rt-owl-carousel[data-carousel-options]')
        super().__init__(page, self.carusel)
        self.strelka = CarouselArrows(page, self.carusel)

    def get_title_uslugi(self):
        title = self.page.locator('.rt-el-title .rtin-title')
        return title.text_content().strip()

    def click__prev(self):
        self.strelka.click_prev()

    def click_next(self):
        self.strelka.click_next()

    def get_all_cart(self) -> list:
        return self.carusel.locator('.rtin-item').all()

    def click_cart_by_title(self, title: str):
        self.carusel.locator(f'.rtin-item:has(h3.item-title a:has-text("{title}"))').first.click()

    def cart_visible_by_title(self, title: str):
        visible_cart = self.carusel.locator(f'.owl-item.active .rtin-item:has(h3.item-title a:has-text("{title}"))')
        return visible_cart.count() > 0

    def scroll_to_item_by_title(self, title):
        for name in range(10):
            if self.cart_visible_by_title(title):
                return True
            self.click_next()
        return False

    def click_item_by_title(self, title: str):
        card = self.carusel.locator(f'.rtin-item:has(h3.item-title a:has-text("{title}"))').first
        card.click()
