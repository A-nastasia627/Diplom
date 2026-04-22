from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class LinkProdoctorov(BaseControl):
    '''Ссылка Prodoctorov'''

    def __init__(self, page: Page, parent_locator: Locator, name: str):
        self.name = name
        self.link = parent_locator.get_by_role("link", name="Prodoctorov")
        super().__init__(page, self.link)

    def click(self):
        self.link.click()
