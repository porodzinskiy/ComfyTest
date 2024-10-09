import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method get current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current URL: {get_url}")

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Value Word OK")

    """Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
        name = f'screenshot{now_date}.png'
        self.driver.save_screenshot(fr'C:\Users\galiz\PycharmProjects\project\screenshots\{name}')

    """Method assert URL"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("URL OK")

    def assert_part(self, str1, str2):
        assert str1 in str2
        print("Value OK")

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S')
        name = f'screenshot{now_date}.png'
        self.driver.save_screenshot(fr'C:\Users\galiz\PycharmProjects\ComfyTest\screenshots\{name}')
