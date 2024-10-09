import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):
    def __init__(self, driver, product_name, product_price):
        super().__init__(driver)
        self.driver = driver
        self.product_name = product_name
        self.product_price = product_price

    """Locators"""
    name = '//div[@class="cart-product-name"]/a'
    price1 = '//div[@class="cart-item-info-price"]/span'
    price2 = '//span[@class="price-total"]'
    price_sum = '//span[@class="total"]'
    checkout_btn = '//span[@class="cart-footer-onepage"]'


    """Getters"""
    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_product_price1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price1)))

    def get_product_price2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price2)))

    def get_product_price_sum(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_sum)))

    def get_checkout_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.checkout_btn)))

    """Actions"""
    def click_checkout_btn(self):
        self.get_checkout_btn().click()
        print("Click Checkout Button")

    def check(self):
        self.assert_part(self.get_product_name().text, self.product_name)
        self.assert_part(self.get_product_price1().text, self.product_price)
        self.assert_part(self.get_product_price2().text, self.product_price)
        self.assert_part(self.get_product_price_sum().text, self.product_price)


    """Methods"""
    def goto_checkout(self):
        self.check()
        self.click_checkout_btn()
        self.assert_url('https://comfy-shop.ru/cart/checkout')