import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""
    city_verify_btn = '//div[@class="current-city-accept-buttons"]/div'
    tv_audio_video_btn = '//a[@class="navigation-first-level-item"][1]'

    """Getters"""
    def get_city_verify_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.city_verify_btn)))

    def get_tv_audio_video_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.tv_audio_video_btn)))

    """Actions"""
    def click_city_verify_btn(self):
        self.get_city_verify_btn().click()
        print("Click City Verify Button")

    def click_tv_audio_video_btn(self):
        self.get_tv_audio_video_btn().click()
        print("Click TV Audio Video Button")

    """Methods"""
    def goto_tv_audio_video(self):
        self.click_city_verify_btn()
        self.click_tv_audio_video_btn()
        self.assert_url('https://comfy-shop.ru/category/televizory-audio-video')