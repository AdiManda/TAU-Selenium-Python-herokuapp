import pytest
import selenium
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    # before test
    global driver
    s = Service(ChromeDriverManager().install())
    driver = selenium.webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.implicitly_wait(2)
    # return driver
    yield driver
    # after test
    driver.quit()

