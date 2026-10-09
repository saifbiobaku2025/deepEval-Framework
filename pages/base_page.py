from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def title(self):
        return self.page.title()

    def screenshot(self, path: str):
        self.page.screenshot(path=path)
