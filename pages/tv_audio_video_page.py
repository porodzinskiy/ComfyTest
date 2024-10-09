import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Tv_audio_video_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""
    tv_btn = '//img[@alt="Телевизоры"]'

    """Getters"""
    def get_tv_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.tv_btn)))

    """Actions"""
    def click_tv_btn(self):
        self.get_tv_btn().click()
        print("Click TV Button")

    """Methods"""
    def goto_tv(self):
        self.click_tv_btn()
        self.assert_url('https://comfy-shop.ru/category/televizory')