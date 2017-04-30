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
        actions = ActionChains(driver)
        username = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        submit = driver.find_element_by_name('submit')
        actions.click(username).send_keys('hassanmamin')
        actions.click(password).send_keys('thisistheadminuser')
        actions.click(submit).perform()
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'username'))
            WebDriverWait(driver, 2).until(element_present)
        except TimeoutException:
            pass

    # @unittest.skip('not now ')
    def test_category_subscribe(self):
        driver.get('http://localhost:8000/app/categories/')
        actions = ActionChains(driver)
        subscribe = driver.find_element_by_class_name('subscribe')
        actions.click(subscribe).perform()
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'category_name'))
            WebDriverWait(driver, 2).until(element_present)
        except TimeoutException:
            pass
        self.assertRegex(driver.current_url,r'categories/[0-9]+$')
        #revert to orignal state
        unsubscribe = driver.find_element_by_class_name('unsubscribe')
        unsubscribe.click()
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'category_name'))
            WebDriverWait(driver, 3).until(element_present)
        except TimeoutException:
            pass

    @unittest.skip('skip now')
    def test_category_unsubscribe(self):
        driver.get('http://localhost:8000/app/categories/')
        actions = ActionChains(driver)
        unsubscribe = driver.find_element_by_class_name('unsubscribe')
        actions.click(unsubscribe).perform()
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'category_name'))
            WebDriverWait(driver, 2).until(element_present)
        except TimeoutException:
            pass
        self.assertRegex(driver.current_url,r'categories/[0-9]+$')
        #revert to orignal state
        subscribe = driver.find_element_by_class_name('subscribe')
        subscribe.click()
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'category_name'))
            WebDriverWait(driver, 3).until(element_present)
        except TimeoutException:
            pass


    def tearDown(self):
        driver.quit()
        pass

unittest.main()
