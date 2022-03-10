import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
import allure
import pytest
import nose2


class PlaceSettingsTest(unittest.TestCase):

    @classmethod
    @allure.severity(allure.severity_level.NORMAL)
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'C:\Users\arbaz.iot\PycharmProjects\TestProject\Drivers\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        sleep(3)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_settings_place(self):
        self.driver.get("https://mevris.io/")
        self.driver.find_element_by_name('email').send_keys('orientpk.mevris@gmail.com')
        self.driver.find_element_by_name('password').send_keys('OELSave80Percent')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/form/div[4]/button/span[1]').click()
        print("1. Login successful")
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        sleep(4)

        place_btn = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div')
        place_btn.click()
        sleep(4)
        print('2. These are the places.Here you can add any new place or control existing one')
        sleep(2)

        Blue_East = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[6]/div')
        Blue_East.click()
        sleep(4)

        place_sett = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[3]/button/span[1]/div')
        place_sett.click()
        sleep(3)

        print('3. These are settings related to a place.You can change anything from here')

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()