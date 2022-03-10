import secrets
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
import HtmlTestRunner
import allure
import pytest
import nose2


class LoginTest(unittest.TestCase):

    @classmethod
    @allure.severity(allure.severity_level.NORMAL)
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'C:\Users\arbaz.iot\PycharmProjects\TestProject\Drivers\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        warnings.filterwarnings("ignore", category=DeprecationWarning)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_valid(self):
        self.driver.get("https://mevris.io/")
        self.driver.find_element_by_name('email').send_keys('orientpk.mevris@gmail.com')
        self.driver.find_element_by_name('password').send_keys('OELSave80Percent')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/form/div[4]/button/span[1]').click()
        print("Login successful")
        sleep(3)
        warnings.filterwarnings("ignore", category=DeprecationWarning)

    @allure.severity(allure.severity_level.NORMAL)
    def test_places(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]').click()
        print('Please select the place')
        sleep(3)

    @allure.severity(allure.severity_level.MINOR)
    def test_qe(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[6]/div').click()
        print('Please select the room')
        sleep(3)

    @allure.severity(allure.severity_level.MINOR)
    def test_room(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[4]').click()
        print('This is the HR room.Here you can control any device')
        sleep(3)

    # def tearDown(self):
        self.driver.close()

    # if __name__ == "__main__":
    #     unittest.main()