from selenium.webdriver.common.by import By

from pageObject.CheckoutPage import CheckOutPage


class HomePage:
    shop = (By.LINK_TEXT, "Shop")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    dropdown_option = (By.ID, "exampleFormControlSelect1")
    radio1_button = (By.ID, "inlineRadio1")
    binding_text = (By.XPATH, "(//input[@type = 'text'])[3]")
    submit = (By.XPATH, "//input[@type = 'submit']")
    alert = (By.CLASS_NAME, "alert.alert-success.alert-dismissible")

    def __init__(self, driver):
        self.driver = driver

    def click_on_shop(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout = CheckOutPage(self.driver)
        return checkout

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def enter_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_dropdown_options(self):
        return self.driver.find_element(*HomePage.dropdown_option)

    def get_radiobutton(self):
        return self.driver.find_element(*HomePage.radio1_button)

    def enter_binding_text(self):
        return self.driver.find_element(*HomePage.binding_text)

    def get_submit(self):
        return self.driver.find_element(*HomePage.submit)

    def get_alert(self):
        return self.driver.find_element(*HomePage.alert)