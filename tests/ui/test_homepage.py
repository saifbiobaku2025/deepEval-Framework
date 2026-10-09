import pytest

from pages.example_page import ExamplePage


@pytest.mark.ui
def test_homepage(page):

    example = ExamplePage(page)

    example.open()

    assert example.title() == "Example Domain"