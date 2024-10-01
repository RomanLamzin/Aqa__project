from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

from pages.cart_page import Cart_page
from pages.main_page import Main_page
from pages.product_page import Product_page
from pages.smartfony_page import Smartfony_page


def test_buy_product():
    driver = webdriver.Chrome()

    print("Тест стартанул")

    mp = Main_page(driver)
    mp.select_catalog_phones()

    sm = Smartfony_page(driver)
    sm.select_product_with_filter_for_samsung()

    pp = Product_page(driver)

    product_price = pp.get_product_price()
    pp.add_product_to_cart()

    cp = Cart_page(driver)
    cp.check_price_in_cart(product_price)





    sleep(4)
    driver.quit()


    # python -m pytest -s -v
