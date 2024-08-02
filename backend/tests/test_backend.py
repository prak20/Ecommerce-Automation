import requests
from backend.utils.logger import logger

def test_amazon_api():
    response = requests.get("https://api.example.com/amazon/search?query=Titan%20watch")
    assert response.status_code == 200
    data = response.json()
    logger.info(f"Amazon API Response: {data}")
    assert "products" in data

def test_flipkart_api():
    response = requests.get("https://api.example.com/flipkart/search?query=Titan%20watch")
    assert response.status_code == 200
    data = response.json()
    logger.info(f"Flipkart API Response: {data}")
    assert "products" in data


