import selenium
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys


class purBeurreTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox("/Users/david/Projets/selenium driver/")
        self.url = "http://127.0.0.1:8000/"
        # self.url = "https://p8-purbeurre-oc.herokuapp.com/"
        self.search = "Nutella"
        self.user = "test@test.com"
        self.password = "password"

    def testSearchPurbeurre(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(5)
        self.elem = self.driver.find_element_by_id("searchForm")
        self.elem.send_keys(self.search)
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.elem = self.driver.find_element_by_id("home")
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

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
