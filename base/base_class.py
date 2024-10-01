import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url  =>>  {get_url}')

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f'Success  -->> вы на странице {result}')

    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y,%m,%d,%H,%M,%S")
        new_screen = f'screenShot {now_date} .png'
        self.driver.save_screenshot(f'..\\screen\\{new_screen}')

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print(f'Url совпал, мы на странице {get_url}')

    """Method assert price by condition"""

    def assert_price_by_condition(self, curPrice, result):
        # value_curPrice = int(curPrice.text.replace(' ', ''))
        value_curPrice = self.convert_money(curPrice)
        assert value_curPrice > result
        print(f'Success  -->> цена выше  {result}')

    """Method assert memory by condition"""

    def assert_memory_by_condition(self, curMemory, result):
        value_curPrice = curMemory.text.split()
        assert str(result) in value_curPrice
        print(f'Success  -->> память телефона   {result} Гб')

    """Method convert money from str to str"""

    def convert_money(self, curPrice):
        return int(curPrice.text.replace(' ', ''))
