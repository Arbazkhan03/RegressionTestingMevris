import warnings
from hashlib import new
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
import allure
import pytest
import select
from selenium.webdriver.common.action_chains import ActionChains


class SettingsButtonTest(unittest.TestCase):

    @classmethod
    @allure.severity(allure.severity_level.NORMAL)
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'C:\Users\arbaz.iot\PycharmProjects\TestProject\Drivers\chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        sleep(3)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_settings_button(self):
        self.driver.get("https://mevris.io/")
        self.driver.find_element_by_name('email').send_keys('orientpk.mevris@gmail.com')
        self.driver.find_element_by_name('password').send_keys('OELSave80Percent')
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/form/div[4]/button/span[1]').click()
        print("Login successful")
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        sleep(3)
        settings_btn = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[1]/div[2]/ul[2]/div/div/div/div/div')
        settings_btn.click()
        sleep(4)

        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/ul/li[1]').click()
        sleep(4)




        # stn = self.driver.find_element('*//li[contains(.,Settings)]')
        # stn.click()
        # sleep(4)




        # select settings_btn =new select(self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div/div/div/div[1]/div[2]/ul[2]/div/div/div/div/div'));
        # settings_btn.selectByVisibleText("Settings");
        # settings_btn.selectByIndex(1);

        # action = ActionChains(self.driver)
        # action.click(on_element=settings_btn).perform()
        # sleep(3)
        # settings_btn.select_by_visible_text('Settings')
        # # settings_btn = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/ul/li[1]/span')
        # # settings_btn.click()
        # # sleep(4)
        print('This is Settings options.You can change the settings from here')

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()