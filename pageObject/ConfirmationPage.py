from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmationPage:

    countryName = (By.ID, "country")
    termsAndConditionsCheckbox = (By.XPATH, "//label[@for = 'checkbox2']")
    purchaseButton = (By.XPATH, "//input[@value = 'Purchase']")
    messageText = (By.XPATH, "//div[@class = 'alert alert-success alert-dismissible']/strong")
    countryNameWait = (By.XPATH, "//div[@class= 'suggestions']")
    countryNameText = (By.XPATH, "ul/li/a")
    def __init__(self, driver):
        self.driver = driver

    def entercontry(self):
        enter_country_name = self.driver.find_element(*ConfirmationPage.countryName)
        return enter_country_name

    def termsandconditions(self):
        checkbox = self.driver.find_element(*ConfirmationPage.termsAndConditionsCheckbox)
        return checkbox

    def purchasebutton(self):
        purchase = self.driver.find_element(*ConfirmationPage.purchaseButton)
        return purchase

    def successmessage(self):
        message = self.driver.find_element(*ConfirmationPage.messageText)
        return message

    def getcontrylist(self):
       # wait = WebDriverWait(self.driver, 10)
       # wait.until(expected_conditions.visibility_of_element_located((ConfirmationPage.countryNameWait)))
        country_list = self.driver.find_elements(*ConfirmationPage.countryNameWait)
        return country_list
