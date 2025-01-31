import pytest
from utils.browser import get_driver

@pytest.fixture
def browser():
    driver = get_driver()
    yield driver
    driver.quit()
