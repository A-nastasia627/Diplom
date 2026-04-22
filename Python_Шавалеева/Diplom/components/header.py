from playwright.sync_api import Page, Locator
from components.base_component import BaseComponent
from components.logo_component import LogoHeader
from controls.navigation_menu import NavigationMenu


class Header(BaseComponent):
    def __init__(self, page: Page):
        self.header = page.locator('#masthead')
        super().__init__(page, self.header)
        self.logo = LogoHeader(page)
        self.navigation = NavigationMenu(page, self.header)

    def click_logo(self):
        self.logo.click()

    def get_menu_link(self, name: str, ) -> Locator:
        return self.navigation.get_menu_link(name)

    def hover_menu(self, name: str):
        self.navigation.hover_menu(name)

    def click_menu_link(self, name: str):
        self.navigation.click_menu_item(name)

    def click_submenu(self, parent_name: str, child_name: str):
        self.navigation.click_submenu(parent_name, child_name)
