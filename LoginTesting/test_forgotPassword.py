import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
import allure
import pytest


class forgotpassword(unittest.TestCase):

    @classmethod
    @allure.severity(allure.severity_level.NORMAL)
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'C:\Users\arbaz.iot\PycharmProjects\TestProject\Drivers\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        sleep(3)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_forgot_password(self):
        self.driver.get("https://mevris.io/")
        fgt_pass = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/form/div[3]/button/span[1]')
        fgt_pass.click()
        print("Please enter the email address associated with your account and we will email you a link to reset your password")
        reset_email = self.driver.find_element_by_name('email')
        reset_email.send_keys('risings974@gmail.com')
        send_link = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/form/div[2]/button/span[1]')
        send_link.click()
        print('Reset Link has been sent to your email address with verification code.Please enter code here')
        sleep(40)
        verify_email = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div[1]/form/div[2]/button/span[1]')
        verify_email.click()

    def tearDown(self):
        sleep(3)
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
