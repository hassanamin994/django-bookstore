from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import unittest
import random

chromedriver = "/home/hassan/Downloads/chromedriver"

os.environ["webdrier.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

class TesAuthentication(unittest.TestCase):
    def setUp(self):
        driver.get('http://localhost:8000/auth/register/')
        self.actions = ActionChains(driver)
        self.username = driver.find_element_by_name('username')
        self.email = driver.find_element_by_name('email')
        self.first_name  = driver.find_element_by_name('first_name')
        self.last_name  = driver.find_element_by_name('last_name')
        self.password  = driver.find_element_by_name('password')
        self.confirm_password  = driver.find_element_by_name('confirm_password')
        self.submit = driver.find_element_by_name('register')
        self.rndstring = str(random.randint(0,50000))

    def test_register_success(self):

        self.actions.click(self.username).send_keys("hassan"+self.rndstring)
        self.actions.click(self.email).send_keys("hassan"+self.rndstring+"@gmail.com")
        self.actions.click(self.first_name).send_keys("hassan")
        self.actions.click_and_hold(self.last_name).release().send_keys("amin")
        self.actions.click(self.password)\
            .send_keys('123456')
        self.actions.click(self.confirm_password)\
            .send_keys('123456')\

        self.actions.click(self.submit).perform()
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'error'))
            WebDriverWait(driver, 2).until(element_present)
        except TimeoutException:
            pass
        self.assertRaises(driver.find_element_by_class_name('errors'),NoSuchElementException)


    def tearDown(self):
        # driver.close()
        pass

unittest.main()
