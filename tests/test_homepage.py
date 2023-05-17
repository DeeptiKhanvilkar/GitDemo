import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObject.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass

# service = Service("C:\Work\Project\Chrome\chromedriver_win32_113\chromedriver.exe")
# driver = webdriver.Chrome(service=service)
service = "C:\Work\Project\Chrome\chromedriver_win32_113\chromedriver.exe"
driver = webdriver.Chrome(executable_path=service)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(10)
driver.maximize_window()


# @pytest.mark.usefixtures("get_variables")
# def test_formsubmision(get_variables):
#     baseclass = BaseClass(driver)
#     log = baseclass.get_logger()
#     homepage = HomePage(driver)
#     time.sleep(5)
#     homepage.get_name().send_keys(get_variables["FirstName"])
#     log.info("Entered Name")
#     homepage.get_email().send_keys(get_variables["Email"])
#     log.info("Entered Email")
#     homepage.enter_password().send_keys(get_variables["Password"])
#     log.info("Entered password")
#     homepage.get_checkbox().click()
#     # static dropbox
#
#     baseclass.select_option(homepage.get_dropdown_options(), get_variables["Gender"])
#     homepage.get_radiobutton().click()
#     homepage.enter_binding_text().send_keys(get_variables["AdditionalText"])
#     homepage.get_submit().click()
#     alert_text = homepage.get_alert().text
#     assert "Success" in alert_text
#     print(alert_text)
#     driver.refresh()


# Following is one of the ways to pass values in methods or in test
# @pytest.fixture(params=[("Deepti", "deeps15th@gmail.com", "Hi", "Female", "Hello"),
#                         ("Ritu", "ritu123@gmail.com", "Message", "Male", "Good Morning")])
# def get_variables(request):
#     return request.param


# @pytest.fixture(params=HomePageData.test_HomePage_data)
# def get_variables(request):
#     return request.param


# *****Second approach *********
@pytest.mark.usefixtures("get_variables")
def test_formsubmision(get_variables):
    print(get_variables)
    baseclass = BaseClass(driver)
    log = baseclass.get_logger()
    homepage = HomePage(driver)
    time.sleep(5)
    homepage.get_name().send_keys(get_variables["FirstName"])
    log.info("Entered Name")
    homepage.get_email().send_keys(get_variables["Email"])
    log.info("Entered Email")
    homepage.enter_password().send_keys(get_variables["Password"])
    log.info("Entered password")
    time.sleep(5)
    homepage.get_checkbox().click()
    # static dropbox

    baseclass.select_option(homepage.get_dropdown_options(), get_variables["Gender"])
    homepage.get_radiobutton().click()
    homepage.enter_binding_text().send_keys(get_variables["AdditionalText"])
    homepage.get_submit().click()
    alert_text = homepage.get_alert().text
    assert "Success" in alert_text
    print(alert_text)
    driver.refresh()


@pytest.fixture(params=HomePageData.get_values_from_excel())
def get_variables(request):
    return request.param