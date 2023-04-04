# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# # import os
# import time
# # import selenium as sl
#
#
# class SeleniumRegisterTest(StaticLiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         # chrome_path = r"
#         # C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
#
#         options = Options()
#         options.binary_location = "C:/Program Files (x86)/Google/Chrome\
#         Application/chrome.exe"
#         # Ceci pour récupérer notre navigateur sur notre OS
#         # geckodriver = os.getcwd() + "/geckodriver"
#         cls.selenium = webdriver.Chrome(chrome_options=options,
#                                         executable_path="C:/Utility/"
#                                                         "BrowserDrivers/"
#                                                         "chromedriver.exe",)
#         cls.selenium.implicitly_wait(10)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super().tearDownClass()
#
#     def test_register(self):
#         self.selenium.get("%s%s" % (self.live_server_url, "/register/"))
#         # On récupère les input pour écrire dans sélénium
#         email_input = self.selenium.find_element(By.NAME, "email")
#         username_input = self.selenium.find_element(By.NAME, "username")
#         password_input = self.selenium.find_element(By.NAME, "password1")
#         confirm_password_input = self.selenium.find_element(By.NAME,
#                                                             "password2")
#         # On écrit dans les inputs
#         email_input.send_keys("user2@gmail.com")
#         username_input.send_keys("user2")
#         password_input.send_keys("passw246")
#         confirm_password_input.send_keys("passw246")
#         # On valide l'inscription
#         time.sleep(4)
#         self.selenium.find_element(By.ID, "subscribe").click()
#         # On vérifie si sur notre page sélénium affichée après l'inscription,
#         # le bouton "mon compte" existe
#         time.sleep(4)
#         account = self.selenium.find_element(By.ID, "mon_compte")
#         assert account
