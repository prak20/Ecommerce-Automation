import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from backend.utils.screenshots import take_screenshot
from backend.utils.params import Config
from frontend.pages.basePage import BasePage

class Flipkart(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def search_product(self, product_name):
        self.driver.get(Config.FLIPKART_URL)
        try:
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._30XB9F'))
            )
            close_button.click()
        except Exception as e:
            print("Login popup not found or already closed:", e)

        search_box=WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
         # search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(product_name + Keys.RETURN)
        # take_screenshot(self.driver, "flipkart_search_results")

    def get_product_details(self):
        prod_details = []
        WebDriverWait(self.driver, 10)  # Wait up to 10 seconds for elements to appear
        # take_screenshot(self.driver, "flipkart_product_details")

        names = self.driver.find_elements(By.CSS_SELECTOR, "a.WKTcLC")
        # name = product.find_element(By.CSS_SELECTOR, "a.IRpwTa").text
        prices = self.driver.find_elements(By.CSS_SELECTOR, "div.Nx9bqj")
        links = self.driver.find_elements(By.CSS_SELECTOR, "a.rPDeLR")

        for name, price, link in zip(names, prices, links):
            prod_details.append({
                'name': name.text,
                'price': price.text,
                'link': link.get_attribute('href')
            })

        return prod_details

    def add_to_cart(self):

        # Get the product details and click on the first product link
        product_details = self.get_product_details()
        if not product_details:
            print("No products found.")
            return

        first_product = product_details[0]["link"]

        # Navigate to the product page
        self.driver.get(first_product)
        # Wait for the page to load and the "Add to Cart" button to be clickable
        wait = WebDriverWait(self.driver, 10)

        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.In9uk2"))
            )
            add_to_cart_button.click()

        except Exception as e:
            print(f'Error during add to cart: {e}')

        print("Product Added to Cart !")
        # take_screenshot(self.driver, "flipkart_add_to_cart")

    def proceed_to_buy(self):
        try:
            close_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._30XB9F'))
            )
            close_button.click()
        except Exception as e:
            print("Login popup not found or already closed:", e)
        buy_now_button = self.driver.find_element(By.CSS_SELECTOR, "button.QqFHMw")
        buy_now_button.click()
        time.sleep(5)  # Sleep for 2 seconds

        # take_screenshot(self.driver, "flipkart_proceed_to_buy")
