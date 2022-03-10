import secrets
import warnings
from selenium import webdriver
from selenium.webdriver.common import actions
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
        place = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]')
        place.click()
        print('Please select the place')
        sleep(3)

    @allure.severity(allure.severity_level.MINOR)
    def test_qe(self):

        place_BE = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[6]/div')
        place_BE.click()
        print('Please select the room')
        sleep(3)

    @allure.severity(allure.severity_level.MINOR)
    def test_room(self):

        # page_3 = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[3]/div/nav/ul/li[4]/button')
        # page_3.click()
        # sleep(4)

        HR_room = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[4]')
        HR_room.click()

        print('This is the First floor HR Room AC.Do you want to change the Mode of AC')
        sleep(5)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_x_heat(self):

        Mode_change = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div[2]/button/span[1]')
        Mode_change.click()
        sleep(3)

        Heat_mode = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/ul/li[3]')
        Heat_mode.click()
        print('Mode Successfully changed to Heat From Cool')
        self.driver.close()


