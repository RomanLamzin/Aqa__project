from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.action = ActionChains(self.driver)

    order_url = 'https://www.citilink.ru/order/'

    # Locators

    add_product_btn = '//button[@data-meta-name="BasketDesktopButton"]'
    cart_btn = '//div[@data-meta-name="BasketButton"]'
    close_popUp_btn = '//button[@data-meta-name="UpsaleBasket__close-popup"]'
    assert_samsung_brand = '(//span[@itemprop="name"])[3]'
    assert_samsung_price = '//span[@class="e1j9birj0 e106ikdt0 app-catalog-8hy98m e1gjr6xo0"]'
    assert_samsung_memory = '(//span[@class="app-catalog-kwpt08 e1g4kseu0"])[3]'

    # Getters

    def get_add_product_btn(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.add_product_btn)))

    def get_cart_btn(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.cart_btn)))

    def get_close_popUp_btn(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.close_popUp_btn)))

    def get_assert_samsung_brand(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.assert_samsung_brand)))

    def get_assert_samsung_price(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.assert_samsung_price)))

    def get_assert_samsung_memory(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.assert_samsung_memory)))

    # Actions

    def click_product_to_cart(self):
        self.get_add_product_btn().click()
        sleep(1)
        self.get_screenshot()

    def click_cart_btn(self):
        self.get_cart_btn().click()
        sleep(1)
        self.get_screenshot()

    def click_close_popUp_btn(self):
        self.get_close_popUp_btn().click()

    # Methods

    def get_product_price(self):
        product_price = self.get_assert_samsung_price()
        return self.convert_money(product_price)

    def add_product_to_cart(self):
        # ПРОВЕРКА ПЕРЕХОДА НА СТРАНИЦУ ПРОДУКТА
        samsung_assert_brand = self.get_assert_samsung_brand()
        self.assert_word(samsung_assert_brand, 'SAMSUNG')

        # ПРОВЕРКА СТОИМОСТИ ПРОДУКТА
        samsung_assert_price = self.get_assert_samsung_price()
        self.assert_price_by_condition(samsung_assert_price, 100000)

        # ПРОВЕРКА ПАМЯТИ ПРОДУКТА
        samsung_assert_memory = self.get_assert_samsung_memory()
        self.assert_memory_by_condition(samsung_assert_memory, 256)

        self.click_product_to_cart()
        self.click_close_popUp_btn()
        self.click_cart_btn()

        sleep(10)

        print('Добавили продукт в корзину и кликнули на переход в неё ')
        self.assert_url(self.order_url)

