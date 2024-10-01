from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.action = ActionChains(self.driver)

    # Locators

    cart_title = '//span[@class="e1ys5m360 e106ikdt0 css-8hy98m e1gjr6xo0"]'
    total_price = '//span[@class="e1j9birj0 e106ikdt0 css-1spb733 e1gjr6xo0"]'

    # Getters

    def get_cart_title(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.cart_title)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))

    # Actions

    # Methods

    def check_price_in_cart(self, priceProduct):
        # ПРОВЕРКА ПРАВЕЛЬНОСТИ СТРАНИЦЫ
        cart_title_val = self.get_cart_title().text
        assert cart_title_val == 'Корзина'
        print('Мы в корзине')

        # ПРОВЕРКА ИТОГОВОЙ СТОИМОСТИ ПРОДУКТА
        cart_price = self.get_total_price()
        samsung_assert_total_price = self.convert_money(cart_price)

        assert samsung_assert_total_price == priceProduct
        print(f'Итогова цена в корзине совпадает с ценой продукта = {priceProduct} руб')
