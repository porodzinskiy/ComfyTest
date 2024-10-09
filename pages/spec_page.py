import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Spec_page(Base):
    def __init__(self, driver, product_name, product_price):
        super().__init__(driver)
        self.product_name = product_name
        self.product_price = product_price
        self.driver = driver

    """Locators"""
    name = '//div[@class="product-main-right-inner"]/div/h1'
    price = '//span[@class="product-price"]'
    add_to_cart_btn = '//button[@class="button btn-cart"]'
    cart_name = '//div[@class="modal-header"]'

    """Getters"""
    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_add_to_cart_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_to_cart_btn)))

    def get_cart_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_name)))

    """Actions"""
    def click_add_to_cart_btn(self):
        self.get_add_to_cart_btn().click()
        print("Click Add To Cart Button")

    def check_spec(self):
        self.assert_word(self.get_product_name(), self.product_name)
        self.assert_word(self.get_product_price(), self.product_price)

    """Methods"""
    def add_to_cart(self):
        self.check_spec()
        self.click_add_to_cart_btn()
        self.assert_part("Ваша корзина", self.get_cart_name().text)
