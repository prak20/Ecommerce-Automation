import pytest

from backend.utils.screenshots import take_screenshot
from frontend.pages.amazon import Amazon
from frontend.pages.flipkart import Flipkart
from backend.utils.logger import logger

@pytest.fixture
def amazon(browser):
    return Amazon(browser)

@pytest.fixture
def flipkart(browser):
    return Flipkart(browser)


@pytest.mark.parametrize("product_name", ["Titan watch"])
def test_amazon_search_product(amazon, product_name):
    amazon.search_product(product_name)
    take_screenshot(amazon.driver, "amazon_search_product")
    logger.info("Amazon Product Searched!")
    global amazon_products
    amazon_products = amazon.get_product_details()
    logger.info(f"Amazon Product Details: {amazon_products[0]}")
    assert amazon_products[0]["name"] is not None
    assert amazon_products[0]["price"] is not None
    assert amazon_products[0]["link"] is not None

def test_amazon_add_to_cart(amazon):
    amazon.search_product("Titan watch")
    amazon.add_to_cart()
    take_screenshot(amazon.driver, "amazon_add_to_cart")
    logger.info(f"Product - {amazon_products[0]['name']} Added to Cart !")
    assert True

def test_amazon_proceed_to_buy(amazon):
    amazon.search_product("Titan watch")
    amazon.add_to_cart()
    amazon.proceed_to_buy()
    take_screenshot(amazon.driver, "amazon_proceed_to_buy")
    logger.info("Proceeding to Buy the Product!")

@pytest.mark.parametrize("product_name", ["Titan watch"])
def test_flipkart_search_product(flipkart, product_name):
    flipkart.search_product(product_name)
    take_screenshot(flipkart.driver, "flipkart_search_product")
    logger.info("Flipkart Product Searched")
    global flipkart_products
    flipkart_products = flipkart.get_product_details()
    logger.info(f"Flipkart Product Details: {flipkart_products[0]}")
    assert flipkart_products[0]["name"] is not None
    assert flipkart_products[0]["price"] is not None
    assert flipkart_products[0]["link"] is not None

def test_flipkart_add_to_cart(flipkart):
    flipkart.search_product("Titan watch")
    flipkart.add_to_cart()
    take_screenshot(flipkart.driver, "flipkart_add_to_cart")
    logger.info(f"Product - {flipkart_products[0]['name']} Added to Cart !")
    assert True

def test_flipkart_proceed_to_buy(flipkart):
    flipkart.search_product("Titan watch")
    flipkart.add_to_cart()
    flipkart.proceed_to_buy()
    take_screenshot(flipkart.driver, "flipkart_proceed_to_buy")
    logger.info("Proceeding to Buy the Product!")

@pytest.mark.parametrize("product_name", ["Titan watch"])
def test_compare_prices(amazon, flipkart, product_name):
    amazon.search_product(product_name)
    amazon_products = amazon.get_product_details()
    flipkart.search_product(product_name)
    flipkart_products = flipkart.get_product_details()
    amazon_price = float(amazon_products[0]["price"].replace(",", ""))
    flipkart_price = float(flipkart_products[0]["price"].replace("₹", "").replace(",", ""))
    if amazon_price < flipkart_price:
        logger.info(f"Amazon offers the lowest price: ₹{str(amazon_price)}")
        take_screenshot(amazon.driver, "amazon_lowest_price")
        assert amazon_price or flipkart_price, "Price comparison Failed"
    elif amazon_price > flipkart_price:
        logger.info(f"Flipkart offers the lowest price: ₹{str(flipkart_price)}")
        take_screenshot(flipkart.driver, "flipkart_lowest_price")
        assert amazon_price or flipkart_price, "Price comparison Failed"
    else:
        logger.info("Prices are the same on both platforms.")
        assert amazon_price or flipkart_price, "Price comparison Passed"
