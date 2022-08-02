import pytest

from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.nomoreparties.site/")

    yield driver

    driver.quit()
