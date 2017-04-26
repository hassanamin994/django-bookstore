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

class TestCategories(unittest.TestCase):
    def setUp(self):
        driver.get('http://localhost:8000/auth/login/')
        self.username = driver.find_element_by_name('username')
        self.password = driver.find_element_by_name('password')
        self.submit = driver.find_element_by_name('submit')
        self.actions = ActionChains(driver)
        self.actions.click(self.username).send_keys('hassanmamin')\
            .click(self.password).send_keys('')\
            .click(self.submit).perform()

        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'navbar-nav'))
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            pass
    def test_subscribe_success(self):

        driver.get('http://localhost:8000/app/categories')
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'unsubscribed'))
            WebDriverWait(driver, 2).until(element_present)
        except TimeoutException:
            pass
        unsubscribed = driver.find_element_by_class_name('unsubscribed')
        if unsubscribed:
            self.actions.click(unsubscribed).perform()


    # def test_unsubcsribe_success(self):
    #     driver.get('http://localhost:8000/app/categories')
    #     subscribed = driver.find_elements_by_class_name('subscribed')
    #     self.actions.click(subscribed).perform()


    def tearDown(self):
        # driver.close()
        pass

unittest.main()
