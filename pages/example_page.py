from pages.base_page import BasePage


class ExamplePage(BasePage):

    URL = "https://example.com"

    def open(self):
        super().open(self.URL)