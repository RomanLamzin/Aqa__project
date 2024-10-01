from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Smartfony_page(Base):
    smartfony_url = 'https://www.citilink.ru/catalog/smartfony/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)

    # Locators

    slider_horizontal = '(//div[@class="rc-slider rc-slider-horizontal"])[2]'
    brand_samsung = '//div[@data-meta-value="SAMSUNG"]'
    built_in_memory = '//div[@data-meta-value="256 ГБ"]'
    select_product_btn = '//div[@data-meta-name="SnippetProductVerticalLayout"]'

    # Getters

    def get_slider_horizontal(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.slider_horizontal)))

    def get_brand_samsung(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.brand_samsung)))

    def get_built_in_memory(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.built_in_memory)))

    def get_select_product_btn(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.select_product_btn)))

    # Actions

    def move_slider_to_right(self):
        local_locator = self.get_slider_horizontal()
        self.driver.execute_script('window.scrollTo(0,500)')
        self.action.click_and_hold(local_locator).move_by_offset(7, 0).release().perform()
        sleep(1)
        self.get_screenshot()

    def click_filter_brand_samsung(self):
        self.driver.execute_script('window.scrollTo(0,1500)')
        self.get_brand_samsung().click()
        sleep(1)
        self.get_screenshot()
        print("Кликнули по brand_samsung = samsung")

    def click_filter_built_in_memory(self):
        self.driver.execute_script('window.scrollTo(0,2000)')
        self.get_built_in_memory().click()
        sleep(1)
        self.get_screenshot()
        print("Кликнули по built_in_memory = 256 ГБ")

    def click_product_btn(self):
        self.driver.execute_script('window.scrollTo(0,0)')
        sleep(2)
        self.get_select_product_btn().click()
        sleep(1)
        self.get_screenshot()
        print("Добавили в корзину телефон")

    # Methods

    def select_product_with_filter_for_samsung(self):
        print("Вошли на  страницу смартфонов")
        self.move_slider_to_right()
        self.click_filter_brand_samsung()
        self.click_filter_built_in_memory()
        self.click_product_btn()
