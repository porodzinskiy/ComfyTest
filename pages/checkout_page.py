import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from faker import Faker

class Checkout_page(Base):
    fake = Faker("ru_RU")
    def __init__(self, driver, product_name, product_price):
        super().__init__(driver)
        self.driver = driver
        self.product_name = product_name
        self.product_price = product_price

    """Locators"""
    first_name = '//input[@id="order-first_name"]'
    last_name = '//input[@id="order-last_name"]'
    phone = '//input[@id="order-phone"]'
    email = '//input[@id="order-email"]'
    order_checkbox = '//input[@id="order-agree"]'
    order_btn = '//button[@id="checkout-cart"]'
    name = '//div[@class="review-item-name"]'
    price1 = '//div[@class="review-item-total"]/span[2]'
    price2 = '//div[@class="text-right"][1]/span'
    price_sum = '//div[@id="checkout-review-table"]/div[2]/div[3]/div[2]/span'

    """Getters"""
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_order_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.order_checkbox)))

    def get_order_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.order_btn)))

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


    """Actions"""
    def input_first_name(self):
        self.get_first_name().send_keys(self.fake.first_name())
        print("Input First Name")

    def input_last_name(self):
        self.get_last_name().send_keys(self.fake.last_name())
        print("Input Last Name")

    def input_phone(self):
        self.get_phone().send_keys(self.fake.phone_number())
        print("Input Phone")

    def input_email(self):
        self.get_email().send_keys(self.fake.email())
        print("Input Email")

    def check(self):
        self.assert_part(self.get_product_name().text, self.product_name)
        self.assert_part(self.product_price[:-1], self.get_product_price1().text)
        self.assert_part(self.product_price[:-1], self.get_product_price2().text)
        self.assert_part(self.product_price[:-1], self.get_product_price_sum().text)

    def click_order_checkbox(self):
        self.get_order_checkbox().click()
        print("Click Order Checkbox")

    def click_order_btn(self):
        self.get_order_btn().click()
        print("Click Order Button")

    """Methods"""
    def goto_order(self):
        self.check()
        self.input_first_name()
        self.input_last_name()
        self.input_phone()
        self.input_email()
        self.get_screenshot()
        self.click_order_checkbox()
        #self.click_order_btn()