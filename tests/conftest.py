import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('Users/kalishka82/BrowserDrivers/chrome.exe')
    # Переходим на страницу авторизации
    pytest.driver.get("http://petfriends.skillfactory.ru/login")

    yield
    pytest.driver.quit()