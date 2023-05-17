# import pytest as pytest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
#
# @pytest.mark.usefixtures("browserInvoke")
# class TestOne:
# from tests.conftest import browserInvoke
#
# def __init__(self, browserInvoke):
#     self.driver = browserInvoke
from pageObject.CheckoutPage import CheckOutPage
from pageObject.ConfirmationPage import ConfirmationPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass

# service = Service("C:\Work\Project\Chrome\chromedriver_win32_113\chromedriver.exe")
# driver = webdriver.Chrome(service=service)

service = "C:\Work\Project\Chrome\chromedriver_win32_113\chromedriver.exe"
driver = webdriver.Chrome(executable_path=service)
# @pytest.mark.usefixtures("browserInvoke")

options = "//div[@class= 'suggestions']"

# from utilities.BaseClass import BaseClass


# class TestDemo(BaseClass):
def test_e2e():
    baseclass =BaseClass(driver)
    log = baseclass.get_logger()
    homepage = HomePage(driver)
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    homepage.click_on_shop()
    log.info("Clicked on shop link")
    # Or //a[contains(@href, 'shop')]  //partial text from link has provided
    #devices_list = driver.find_elements(By.XPATH, "//div[@class = 'card h-100']")
    checkout = CheckOutPage(driver)
    #checkout = HomePage.clickonshop()
    device_list = checkout.listOfItem()
    for i in device_list:
        # product_name = i.find_element(By.XPATH, "div/h4/a").text
        product_name = i.find_element(*CheckOutPage.productName).text
        if product_name == "Samsung Note 8":
            i.find_element(*CheckOutPage.addCart).click()
            log.info("Clicked on given device's add cart")
            break
        else:
            log.debug("no a product which you are searching")
    #checkout.getproductname()
    confirmation = ConfirmationPage(driver)
    checkout = CheckOutPage(driver)
    checkout.firstcheckout()
    checkout.finalcheckout()
    confirmation.entercontry().send_keys("Ind")
    baseclass = BaseClass(driver)
    baseclass.waitforelemt(options)
    country_list = confirmation.getcontrylist()
    for i in country_list:
        country = i.find_element(*ConfirmationPage.countryNameText).text
        if country == 'India':
            i.find_element(*ConfirmationPage.countryNameText).click()
        else:
            print("fail")

    confirmation.termsandconditions().click()
    confirmation.purchasebutton().click()
    success_msg = confirmation.successmessage().text
    assert "Success" in success_msg
    time.sleep(10)
