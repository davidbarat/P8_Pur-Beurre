from django.test import RequestFactory
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core import mail
from django.http import request, HttpRequest
from django.utils.http import base36_to_int, int_to_base36
from django.utils.http import urlsafe_base64_encode
from django.db.models.query_utils import Q
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model

import selenium
import unittest
import time
import os
import requests, re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def password_reset_confirm_url(uidb64, token):
        try:
            print(reverse("password_reset_confirm", args=(uidb64, token)))
            return reverse("password_reset_confirm", args=(uidb64, token))
        except NoReverseMatch:
            return f"/accounts/reset/invaliduidb64/invalid-token/"

# @override_settings(EMAIL_BACKEND='django.core.mail.backends.filebased.EmailBackend')
class purBeurreTest(unittest.TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.factory = RequestFactory()
        cls.user = User.objects.create_user(
            email="test3@test.te",
            password="test123",
            first_name="Test",
            last_name="test",
            username="Tester",
        )
        cls.user.save()
    
    def setUp(self):
        if os.environ.get("ENV") == "DEV":
            self.driver = webdriver.Firefox("/Users/david/Projets/selenium driver/")
            self.url = "http://127.0.0.1:8000/"
            self.driver.maximize_window()

        else:
            self.BROWSERSTACK_URL = 'https://davidbarat1:FxhRcmmHYxhSpVrjeAWu@hub-cloud.browserstack.com/wd/hub'
            self.desired_cap = {
                'os' : 'Windows',
                'os_version' : '10',
                'browser' : 'Chrome',
                'browser_version' : '80',
                'name' : "P8 Test"
                }
            self.driver = webdriver.Remote(
                command_executor=self.BROWSERSTACK_URL,
                desired_capabilities=self.desired_cap)
            self.driver.maximize_window()

            self.url = "http://167.99.212.10/"

        self.search = "Nutella"
        self.user = "test@test.com"
        self.password = "password"
        self.newpassword = "newpassword"
        self.mailtrap = '1dd21617c6-94031c@inbox.mailtrap.io'
        self.apikey = 'af525dcfe5f912d634cca848ee2921d4'
        self.inboxid = '1222935'
        self.urlmail = "https://mailtrap.io/api/v1/"
        self.payload = {"api_token" : self.apikey}
        """
        self.user = User.objects.create_user(
            email="test3@test.te",
            password="test123",
            first_name="Test",
            last_name="test",
            username="Tester",
        )
        self.user.save()
        """
        self.user_filter = User.objects.filter(Q(email=self.user))
        print(self.user_filter)
        self.token = default_token_generator.make_token(self.user_filter.pk)
        print(self.token)
        self.uid = urlsafe_base64_encode(force_bytes(self.user_filter.pk))
        print(self.uid)


    def testSearchPurbeurre(self):
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
        # self.driver.maximize_window()
        self.driver.get(self.url)
        self.elem = self.driver.find_element_by_id("myproducts")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.elem = self.driver.find_element_by_id("id_username")
        self.elem.send_keys(self.user)
        self.elem = self.driver.find_element_by_id("id_password")
        self.elem.send_keys(self.password)
        self.elem.send_keys(Keys.RETURN)
        time.sleep(8)
        """
        self.wait = WebDriverWait(self.driver, 120)
        self.elem = self.driver.find_element_by_id("logout")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        """

    def testMentionsContacts(self):
        # self.driver.maximize_window()
        self.driver.get(self.url)
        self.elem = self.driver.find_element_by_id("mentions")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.elem = self.driver.find_element_by_id("contact")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)

    """
    def testChangePassword(self):
        # self.driver.maximize_window()
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
    """
    # @override_settings(EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend')
    def testResetPassword(self):
        # self.driver.maximize_window()
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
        self.elem = self.driver.find_element_by_id("logout")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(3)
        self.elem = self.driver.find_element_by_id("login")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(5)
        self.elem = self.driver.find_element_by_id("resetpassword")
        self.elem.send_keys(Keys.RETURN)
        time.sleep(3)
        self.elem = self.driver.find_element_by_id("id_email")
        self.elem.send_keys(self.user)
        time.sleep(3)
        self.user_filter = User.objects.filter(Q(username=self.user))
        # User = get_user_model()
        # self.users = User.objects.all()
        # print(self.users)
        # self.user_filter = User.objects.get(email__iexact='test3@test.te')
        
        self.driver.get("/reset/%s/%s/" % (self.uid, self.token))
        self.driver.get(password_reset_confirm_url(self.uid, self.token))
        self.driver.find_element_by_name("password1").send_keys("password")
        self.driver.find_element_by_name("password2").send_keys("password")
        self.driver.find_element_by_name("action").submit()
        """
        for self.user in self.user_filter:
            print(self.user)
            self.token = default_token_generator.make_token(self.user.pk)
            print(self.token)
            self.uid = urlsafe_base64_encode(force_bytes(self.user.pk))
            print(self.uid)
            self.driver.get("/reset/%s/%s/" % (self.uid, self.token))
            self.driver.get(password_reset_confirm_url(self.uid, self.token))
            self.driver.find_element_by_name("password1").send_keys("password")
            self.driver.find_element_by_name("password2").send_keys("password")
            self.driver.find_element_by_name("action").submit()
        """
        # print(self.meta)
        self.r = requests.patch(
                        url=self.urlmail + "inboxes/" + str(self.inboxid) + "/clean",
                        params=self.payload,
                        headers={
                            "UserAgent": "Project Purbeurre - MacOS - Version 10.13.6"
                        },
                    )
        
        self.r = requests.get(
                        url=self.urlmail + "inboxes/" + str(self.inboxid) + "/messages",
                        params=self.payload,
                        headers={
                            "UserAgent": "Project Purbeurre - MacOS - Version 10.13.6"
                        },
                    )
        # self.param = request.resolver_match.kwargs.get('url_param')
        # print(self.param)
        
        """
        self.data = self.r.json()
        print(self.data)
        """
        # self.msg = mail.outbox[0]
        # self.idmsg = self.data.id
        # 
        # self.url = utils_extract_reset_tokens(self.msg.body)
        # self.extract_url = self.url[0]
        """
        self.driver.get(
            "https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")
        self.elem = self.driver.find_element_by_xpath('//*[@id ="identifierId"]')
        self.elem.send_keys('dav.barat@gmail.com')
        self.elem = self.driver.find_elements_by_xpath('//*[@id ="identifierNext"]') 
        self.elem[0].click()
        time.sleep(3)
        self.elem = self.driver.find_element_by_xpath('//*[@id ="password"]/div[1]/div / div[1]/input') 
        self.elem.send_keys('Selmer!25') 
        self.elem = self.driver.find_elements_by_xpath('//*[@id ="passwordNext"]') 
        self.elem[0].click()
        """

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
    unittest.main(warnings='ignore')
