from locust import TaskSet, task, HttpUser, between
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from frontend.pages.amazon import Amazon
from frontend.pages.flipkart import Flipkart


class EcomPerformance(TaskSet):

    def setup_browser(self):
        options = Options()
        options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(options=options)
        self.amazon = Amazon(self.browser)
        self.flipkart = Flipkart(self.browser)

    def teardown_browser(self):
        self.browser.quit()

    def on_start(self):
        self.setup_browser()

    def on_stop(self):
        self.teardown_browser()

    @task(1)
    def perform_amazon_search(self):
        self.amazon.search_product("Titan watch")
        products = self.amazon.get_product_details()
        if products:
            print(f"Amazon search results: {products[0]['name']}")

    @task(1)
    def perform_flipkart_search(self):
        self.flipkart.search_product("Titan watch")
        products = self.flipkart.get_product_details()
        if products:
            print(f"Flipkart search results: {products[0]['name']}")

    @task(1)
    def add_product_to_cart_amazon(self):
        self.amazon.search_product("Titan watch")
        self.amazon.add_to_cart()
        print("Product added to Amazon cart")

    @task(1)
    def add_product_to_cart_flipkart(self):
        self.flipkart.search_product("Titan watch")
        self.flipkart.add_to_cart()
        print("Product added to Flipkart cart")

    @task(1)
    def proceed_to_checkout_amazon(self):
        self.amazon.search_product("Titan watch")
        self.amazon.add_to_cart()
        self.amazon.proceed_to_buy()
        print("Proceeded to checkout on Amazon")

    @task(1)
    def proceed_to_checkout_flipkart(self):
        self.flipkart.search_product("Titan watch")
        self.flipkart.add_to_cart()
        self.flipkart.proceed_to_buy()
        print("Proceeded to checkout on Flipkart")


class EcommerceUser(HttpUser):
    tasks = [EcomPerformance]
    wait_time = between(2, 10)
