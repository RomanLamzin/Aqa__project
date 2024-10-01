from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Main_page(Base):
    main_url = 'https://www.citilink.ru/'
    smartfony_url = "https://www.citilink.ru/catalog/smartfony/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog_phones = '//a[@data-meta-category="cardId-2"]'

    # Getters

    def get_catalog_phones(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.catalog_phones)))

    # Actions

    def click_catalog_phones(self):
        self.get_catalog_phones().click()
        print("Кликнули по catalog_phones")

    # Methods

    def select_catalog_phones(self):
        self.driver.get(self.main_url)
        self.driver.maximize_window()
        print("Вошли на главную страницу")
        self.click_catalog_phones()
        self.assert_url(self.smartfony_url)

