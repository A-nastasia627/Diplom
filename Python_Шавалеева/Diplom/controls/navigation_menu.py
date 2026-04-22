from playwright.sync_api import Page, Locator, expect
from controls.base_control import BaseControl


class NavigationMenu(BaseControl):
    '''Главное навигационное меню и подменю'''
    def __init__(self, page: Page, parent_locator: Locator):
        self.menu = parent_locator
        super().__init__(page, self.menu)

    def get_menu_link(self, name: str):
        return self.menu.get_by_role("link", name=name).first

    def get_menu_item(self, name: str):
        return self.menu.locator(f'li.menu-item:has(a:has-text("{name}"))').first

    def hover_menu(self, name: str):
        self.get_menu_link(name).hover()

    def click_menu_item(self, name: str):
        self.get_menu_link(name).click()

    def click_submenu(self, parent_name: str, child_name: str):
        parent_item = self.get_menu_item(parent_name)
        parent_item.hover()
        child_link = self.menu.get_by_role("link", name=child_name).first
        expect(child_link).to_be_visible(timeout=3000)
        child_link.click()
