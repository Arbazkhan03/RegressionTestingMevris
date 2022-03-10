import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
import allure
import pytest


class SignUpTest(unittest.TestCase):

    @classmethod
    @allure.severity(allure.severity_level.NORMAL)
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'C:\Users\arbaz.iot\PycharmProjects\TestProject\Drivers\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        sleep(3)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_InValid_SignUp(self):
        self.driver.get("https://mevris.io/")
        sign_up = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]/a/button/span[1]')
        sign_up.click()
        f_name = self.driver.find_element_by_name('firstName')
        f_name.send_keys("Automation")
        l_name = self.driver.find_element_by_name('lastName')
        l_name.send_keys('testing')
        email = self.driver.find_element_by_name('email')
        email.send_keys('khan.arbaz0303@gmail')
        pswrd = self.driver.find_element_by_name('password')
        pswrd.send_keys('Test')
        cnfrm_pswrd = self.driver.find_element_by_name('confirmPassword')
        cnfrm_pswrd.send_keys('Test@123')
        btn_signup = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/form/div[5]/button/span[1]')
        btn_signup.click()
        sleep(3)
        print("You have provided the incorrect details")
        sleep(3)

    def tearDown(self):

        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
