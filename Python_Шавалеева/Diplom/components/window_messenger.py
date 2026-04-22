from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class WindowMessenger(BaseComponent):
    '''Окно, чат для связи'''
    def __init__(self, page: Page):
        self.window_chat = page.locator("#mvvwo_chat_box")
        super().__init__(page, self.window_chat)

    def get_title(self):
        return self.window_chat.locator("#mvvwo_chat_head")

    def get_status(self):
        return self.window_chat.locator(".mvvwo_online")

    def get_input(self):
        return self.window_chat.locator("#mvvwo_chatSend")

    def get_text_in_window(self):
        return self.window_chat.locator(".mvvwo_chat_body p")

    def get_button_close(self):
        return self.window_chat.locator("span.mvvwo_chat_close")

    def click_button_close(self):
        self.get_button_close().click()

    def get_send_button(self):
        return self.window_chat.locator("a#mvvwo_fab_send")

    def click_button_send(self):
        self.get_send_button().click()

    def clear_message(self, text: str):
        input_field = self.get_input()
        input_field.fill(text)
