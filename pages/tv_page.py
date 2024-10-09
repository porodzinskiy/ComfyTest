import time
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Tv_page(Base):

    max_price = 29000 #Макисмальная цена
    min_size = 55 #Минимальный размер экрана
    first_tv_url = 'https://comfy-shop.ru/55-televizor-starwind-sw-led55ug400' #Самый дешевый подходящий телевизор (для проверки)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""
    max_price_input = '//input[@id="priceEnd"]'
    min_size_input = '//input[@name="attr01756[from]"]'
    yandex_tv_checkbox = '//a[contains(text(), "Яндекс ТВ")]'
    find_btn = '//a[@id="parts"]'
    product_name = '//div[@class="products-name"]'
    product_price = '//span[@class="product-price-value"]'
    open_spec_btn = '//div[@id="products"]/ul/div[1]/div[4]/a/img'

    """Getters"""
    def get_max_price_input(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.max_price_input)))

    def get_min_size_input(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.min_size_input)))

    def get_yandex_tv_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.yandex_tv_checkbox)))

    def get_find_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.find_btn)))

    def get_open_spec_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.open_spec_btn)))

    def get_product_name(self, i):
        return WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, f'//div[@id="products"]/ul/div[{i}]/div[5]/a')))

    def get_product_price(self, i):
        return WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, f'//div[@id="products"]/ul/div[{i}]/div[7]/div[1]/div/span/span')))

    def get_cart_word(self):
        return WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_word)))

    """Actions"""
    def input_max_price(self, max_price):
        self.get_max_price_input().clear()
        self.get_max_price_input().send_keys(max_price)
        print("Input Max Price")

    def input_min_size(self, min_size):
        self.get_min_size_input().clear()
        self.get_min_size_input().send_keys(min_size)
        print("Input Min Size")

    def click_yandex_tv_checkbox(self):
        self.get_yandex_tv_checkbox().click()
        print("Click Yandex TV Checkbox")

    def click_find_btn(self):
        self.get_find_btn().click()
        print("Click Find Btn")

    def check_filters(self):
        i = 1
        good = True
        while True:
            try:
                product_name = self.get_product_name(i).text
                product_price = self.get_product_price(i).text
            except exceptions.TimeoutException:
                break
            if not int(product_name[:2]) >= self.min_size:
                good = False
            if not int(product_price[:-1]) <= self.max_price:
                good = False
            i += 1
        if good:
            print("Filters OK")
        else:
            print("Filters ERROR")

    def click_open_spec(self):
        self.get_open_spec_btn().click()
        print("Click Open Specification")

    """Methods"""
    def filters(self):
        self.input_max_price(self.max_price)
        self.input_min_size(self.min_size)
        self.click_yandex_tv_checkbox()
        self.click_find_btn()
        time.sleep(1)
        self.check_filters()

    def to_cart(self):
        product_name = self.get_product_name(1).text
        product_price = self.get_product_price(1).text
        self.click_open_spec()
        self.assert_url(self.first_tv_url)
        return product_name, product_price
