import pytest

@pytest.mark.ui
def test_homepage(app_page):
    assert app_page.title() == "Example Domain"