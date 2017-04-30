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
        pass


    def test_register_success(self):
        driver.get('http://localhost:8000/auth/register/')
        actions = ActionChains(driver)
        username = driver.find_element_by_name('username')
        email = driver.find_element_by_name('email')
        first_name  = driver.find_element_by_name('first_name')
        last_name  = driver.find_element_by_name('last_name')
        password  = driver.find_element_by_name('password')
        confirm_password  = driver.find_element_by_name('confirm_password')
        submit = driver.find_element_by_name('register')
        rndstring = str(random.randint(0,50000))
        actions.click(username).send_keys("hassan"+rndstring)
        actions.click(email).send_keys("hassan"+rndstring+"@gmail.com")
        actions.click(first_name).send_keys("hassan")
        actions.click_and_hold(last_name).release().send_keys("amin")
        actions.click(password)\
            .send_keys('123456')
        actions.click(confirm_password)\
            .send_keys('123456')\

        actions.click(submit).perform()
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'username'))
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            pass
        self.assertRegex(driver.current_url,r'login')

    def test_register_fail(self):
        driver.get('http://localhost:8000/auth/register/')
        actions = ActionChains(driver)
        username = driver.find_element_by_name('username')
        email = driver.find_element_by_name('email')
        first_name  = driver.find_element_by_name('first_name')
        last_name  = driver.find_element_by_name('last_name')
        password  = driver.find_element_by_name('password')
        confirm_password  = driver.find_element_by_name('confirm_password')
        submit = driver.find_element_by_name('register')
        rndstring = str(random.randint(0,50000))
        actions.click(username).send_keys("hassan"+rndstring)
        actions.click(email).send_keys("hassan"+rndstring+"@gmail.com")
        actions.click(first_name).send_keys("hassan")
        actions.click_and_hold(last_name).release().send_keys("amin")
        actions.click(password)\
            .send_keys('1234567')
        actions.click(confirm_password)\
            .send_keys('123456')\

        actions.click(submit).perform()
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'username'))
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            pass
        self.assertRegex(driver.current_url,r'register')

    def test_login_success(self):
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
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            pass
        self.assertRegex(driver.current_url,r'app')
        logout = driver.find_element_by_id('logout')
        logout.click()

    def test_login_fail(self):
        driver.get('http://localhost:8000/auth/login/')
        actions = ActionChains(driver)
        username = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        submit = driver.find_element_by_name('submit')
        actions.click(username).send_keys('hassanmamin')
        actions.click(password).send_keys('thisiswrongpassword')
        actions.click(submit).perform()
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'username'))
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            pass
        self.assertRegex(driver.current_url,r'auth')


    def tearDown(self):
        # driver.quit()
        pass

unittest.main()
