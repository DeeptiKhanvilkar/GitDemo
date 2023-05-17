from selenium.webdriver.common.by import By

from pageObject.ConfirmationPage import ConfirmationPage


class CheckOutPage:
    devicesList = (By.XPATH,"//div[@class = 'card h-100']")
    firstCheckout = (By.XPATH, "//li[@class = 'nav-item active']/a")
    finalCheckout = (By.XPATH, "//tbody/tr[3]/td[5]/button")
    productName =(By.XPATH, "div/h4/a")
    addCart = (By.XPATH, "//div[2]/button")

    def __init__(self,driver):
        self.driver = driver

    def listOfItem(self):
        device_list = self.driver.find_elements(*CheckOutPage.devicesList)
        #devices_list = driver.find_elements(By.XPATH, "//div[@class = 'card h-100']")
        return device_list

    # def getproductname(self):
    #     device_list = CheckOutPage.listOfItem(self)


    def firstcheckout(self):
        self.driver.find_element(*CheckOutPage.firstCheckout).click()

    def finalcheckout(self):
        self.driver.find_element(*CheckOutPage.finalCheckout).click()
        confirmation = ConfirmationPage(self.driver)
        return confirmation