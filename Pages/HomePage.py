from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.user_dropdown_xpath = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
        self.logout_xpath = "//a[normalize-space()='Logout']"

    def click_on_user_dropdown(self):
        self.driver.find_element(By.XPATH, self.user_dropdown_xpath).click()

    def click_on_logout(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()

