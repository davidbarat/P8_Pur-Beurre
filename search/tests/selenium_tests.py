import selenium
from selenium import webdriver
import unittest
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class purBeurreTest(unittest.TestCase):
    def setUp(self):
        if os.environ.get("ENV") == "DEV":
            self.driver = webdriver.Firefox("/Users/david/Projets/selenium driver/")
            self.url = "http://127.0.0.1:8000/"
        else:
            self.driver = webdriver.Firefox("/home/travis/build/davidbarat/P8_Pur-Beurre/geckodriver")
            self.url = "http://167.99.212.10/"
        self.search = "Nutella"
        self.user = "test@test.com"
        self.password = "password"
        self.newpassword = "newpassword"

    def testSearchPurbeurre(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(5)
        self.elem = self.driver.find_element_by_id("login")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.elem = self.driver.find_element_by_id("id_username")
        self.elem.send_keys(self.user)
        self.elem = self.driver.find_element_by_id("id_password")
        self.elem.send_keys(self.password)
        self.elem.send_keys(Keys.RETURN)
        time.sleep(3)
        self.elem = self.driver.find_element_by_id("searchForm")
        self.elem.send_keys(self.search)
        self.elem.send_keys(Keys.RETURN)
        time.sleep(3)
        self.wait = WebDriverWait(self.driver, 120)
        self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "//a[text()='Sauvegardez']"))).click()
        self.elem = self.driver.find_element_by_id("myproducts")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        
    def testMyProducts(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.elem = self.driver.find_element_by_id("myproducts")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.elem = self.driver.find_element_by_id("id_username")
        self.elem.send_keys(self.user)
        self.elem = self.driver.find_element_by_id("id_password")
        self.elem.send_keys(self.password)
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.wait = WebDriverWait(self.driver, 120)
        self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "//alt[text()='Sauvegardez']"))).click()
        self.elem = self.driver.find_element_by_id("logout")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)

    def testMentionsContacts(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.elem = self.driver.find_element_by_id("mentions")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.elem = self.driver.find_element_by_id("contact")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)

    def testChangePassword(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(5)
        self.elem = self.driver.find_element_by_id("login")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.elem = self.driver.find_element_by_id("id_username")
        self.elem.send_keys(self.user)
        self.elem = self.driver.find_element_by_id("id_password")
        self.elem.send_keys(self.password)
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.elem = self.driver.find_element_by_id("moncompte")
        self.elem.send_keys(self.password)
        self.elem.send_keys(Keys.RETURN)
        time.sleep(3)
        self.elem = self.driver.find_element_by_id("changepassword")
        self.elem.send_keys(self.search)
        self.elem.send_keys(Keys.RETURN)
        time.sleep(3)
        self.elem = self.driver.find_element_by_id("id_old_password")
        self.elem.send_keys(self.password)
        self.elem = self.driver.find_element_by_id("id_new_password1")
        self.elem.send_keys(self.newpassword)
        self.elem = self.driver.find_element_by_id("id_new_password2")
        self.elem.send_keys(self.newpassword)
        self.elem.send_keys(Keys.RETURN)
        # change to initial password
        self.elem = self.driver.find_element_by_id("moncompte")
        self.elem.send_keys(self.password)
        self.elem.send_keys(Keys.RETURN)
        time.sleep(3)
        self.elem = self.driver.find_element_by_id("changepassword")
        self.elem.send_keys(self.search)
        self.elem.send_keys(Keys.RETURN)
        time.sleep(3)
        self.elem = self.driver.find_element_by_id("id_old_password")
        self.elem.send_keys(self.newpassword)
        self.elem = self.driver.find_element_by_id("id_new_password1")
        self.elem.send_keys(self.password)
        self.elem = self.driver.find_element_by_id("id_new_password2")
        self.elem.send_keys(self.password)
        self.elem.send_keys(Keys.RETURN)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
