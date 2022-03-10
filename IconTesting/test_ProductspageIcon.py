import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
import allure
import pytest


class ProductsPageIconTest(unittest.TestCase):

    @classmethod
    @allure.severity(allure.severity_level.NORMAL)
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'C:\Users\arbaz.iot\PycharmProjects\TestProject\Drivers\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        sleep(3)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_productspage_Icon(self):
        self.driver.get("https://mevris.io/")
        self.driver.find_element_by_name('email').send_keys('orientpk.mevris@gmail.com')
        self.driver.find_element_by_name('password').send_keys('OELSave80Percent')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/form/div[4]/button/span[1]').click()
        print("Login successful")
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        sleep(5)
        products_btn = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[1]/div[2]/ul[1]/div[3]/div/div')
        products_btn.click()
        sleep(3)
        print('These are the products in the Mevris application that you can add and manipulate')

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()