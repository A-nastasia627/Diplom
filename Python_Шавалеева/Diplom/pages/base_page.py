from playwright.sync_api import expect


class BasePage:
    def __init__(self, page, url):
        self.page = page
        self.url = url

    def open(self):
        return self.page.goto(self.url)

    def check_title_h1(self, title: str):
        expect(self.page.locator('h1.entry-title')).to_have_text(title)
