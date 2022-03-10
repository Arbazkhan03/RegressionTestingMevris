import secrets
import warnings
from selenium import webdriver
from selenium.webdriver.common import actions, window
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
import HtmlTestRunner
import allure
import pytest


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

        HR_room = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[4]')
        HR_room.click()

        print('This is the First floor HR Room AC.Do you want to Turn on the Auto-Pilot Mode of AC')
        sleep(4)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_x_AutoPilot(self):

        # window.scrollTo(0, 200)
        # self.driver.execute_script("window.scrollTo(0, 1080)")
        # print('44')
        # self.driver.close()
        window.scrollTo(0, 200)
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 400)")
        sleep(2)

        mode = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div[2]')
        mode.click()
        sleep(4)

        btn_on = self.driver.find_element(By.XPATH("/html/body/div[3]/div[3]/div/div/div/div/div[2]/div[2]/div[1]/span/span[2]"))
        btn_on.click()
        sleep(4)
        print('Auto-Pilot mode has been turned on/off successfully')
        self.driver.close()


#       self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # page = self.driver.find_elements_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div/div')
        # page.send_keys(Keys.PAGE_DOWN)
