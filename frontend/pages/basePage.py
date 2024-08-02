from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service

class BasePage:
    def __init__(self, driver: WebDriver):
    # def __init__(self):
    #     # Path to your chromedriver in the project directory
    #     chrome_driver_path = '../../chromedriver.exe'  # or './chromedriver.exe' for Windows
    #     options = webdriver.ChromeOptions()
    #     # Add any necessary options here
    #     # options.add_argument('--headless')  # Uncomment to run in headless mode
    #     service = Service(chrome_driver_path)
    #     driver = webdriver.Chrome(service=service, options=options)
        self.driver = driver

    def find_element(self, by: By, value: str):
        return self.driver.find_element(by, value)

    def find_elements(self, by: By, value: str):
        return self.driver.find_elements(by, value)