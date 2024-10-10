import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage

class LoginTest(unittest.TestCase):
    # Run Setup only once before all the test methods, use @classmethod as setUpClass method belongs to the class
    @classmethod
    def setUpClass(cls) -> None:
        cls.chrome_serv_obj = Service("C:\Drivers\webdriver\chromedriver-win64\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.chrome_serv_obj)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login_valid(self) -> None:
        url = "https://opensource-demo.orangehrmlive.com/"
        self.driver.get(url)
        login = LoginPage(self.driver)
        login.enter_username("admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(self.driver)
        homepage.click_on_user_dropdown()
        homepage.click_on_logout()

        # self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("admin")
        # self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        #
        # time.sleep(5)
        #
        # self.driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
        # self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        #
        # time.sleep(5)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Login Test completed")
