import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture()
def set_up():
    print("\t\tStart Test")

    url = 'https://comfy-shop.ru/'
    options = Options()
    #options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.maximize_window()

    yield driver

    print("\t\tFinish Test")

