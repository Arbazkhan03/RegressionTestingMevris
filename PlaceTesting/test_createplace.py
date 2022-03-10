import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
import allure
import pytest


class CreatePlaceTest(unittest.TestCase):

    @classmethod
    @allure.severity(allure.severity_level.NORMAL)
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'C:\Users\arbaz.iot\PycharmProjects\TestProject\Drivers\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        sleep(3)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_create_place(self):
        self.driver.get("https://mevris.io/")
        self.driver.find_element_by_name('email').send_keys('orientpk.mevris@gmail.com')
        self.driver.find_element_by_name('password').send_keys('OELSave80Percent')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/form/div[4]/button/span[1]').click()
        print("Login successful")
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        sleep(4)

        place_btn = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div')
        place_btn.click()
        sleep(4)
        print('These are the places.Here you can add any new place or control existing one')
        sleep(2)
        create_place = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[3]/button/span[1]/div')
        create_place.click()
        sleep(2)
        print('Please put the name of the place')

        place_name = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div/input')
        place_name.send_keys('TestingPlace')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]').click()
        print('Please select the type of the place')
        sleep(2)

        type_place = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div/div/div[6]/div/div/span')
        type_place.click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[2]/button/span[1]').click()
        sleep(3)
        print('Place created successfully')

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()