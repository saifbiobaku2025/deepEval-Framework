import pytest
@pytest.mark.ui

def test_homepage(example_page):
    assert example_page.title() == "Example Domain"
