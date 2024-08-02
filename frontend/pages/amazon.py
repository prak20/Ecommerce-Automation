import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from backend.utils.screenshots import take_screenshot
from backend.utils.params import Config
from frontend.pages.basePage import BasePage


class Amazon(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def search_product(self, product_name):
        self.driver.get(Config.AMAZON_URL)
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(product_name + Keys.RETURN)
        # take_screenshot(self.driver, "amazon_search_results")

    def get_product_details(self):

        prod_details = []

        WebDriverWait(self.driver, 10)  # Wait up to 10 seconds for elements to appear

        products = self.find_elements(By.CSS_SELECTOR, 'div.s-main-slot div.s-result-item')

        # take_screenshot(self.driver, "amazon_product_details")

        for product in products:
            try:
                product_name = product.find_element(By.CSS_SELECTOR, 'span.a-text-normal').text
                product_price = product.find_element(By.CSS_SELECTOR, 'span.a-price-whole').text
                product_link = product.find_element(By.CSS_SELECTOR, 'a.a-link-normal').get_attribute('href')

                prod_details.append({
                    'name': product_name,
                    'price': product_price,
                    'link': product_link
                })
            except Exception as e:
                # Log or handle exception if product details are not found
                print(f'Error fetching details: {e}')

        print(prod_details[0])

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
                EC.element_to_be_clickable((By.ID, "add-to-cart-button"))
            )
            add_to_cart_button.click()

            # Handle potential additional prompts
            try:
                wait = WebDriverWait(self.driver, 5)
                # Wait for the "Add Protection" or similar prompt to appear
                skip_button = wait.until(
                    EC.element_to_be_clickable((By.ID, "attachSiNoCoverage"))
                )

                if skip_button:
                    print("Protection/Skip option found, clicking Skip...")
                    skip_button.click()


            except Exception as e:
                print("No Protection/Skip option found or an error occurred:", e)

            go_to_cart = wait.until(EC.element_to_be_clickable((By.ID, "sw-gtc")))
            go_to_cart.click()

        except Exception as e:
            print(f'Error during add to cart: {e}')

        print("Product Added to Cart !")
        # take_screenshot(self.driver, "amazon_add_to_cart")


    def proceed_to_buy(self):

        buy_btn = self.driver.find_element(By.NAME, "proceedToRetailCheckout")
        buy_btn.click()
        time.sleep(5)  # Sleep for 2 seconds
        # take_screenshot(self.driver, "amazon_proceed_to_buy")

