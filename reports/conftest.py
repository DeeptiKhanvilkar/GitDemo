import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )

# def pytest_addoption(parser):
#     parser.addoption(
#         "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
#     )


@pytest.fixture()
def setup(request):
    #global driver
    browser_name = request.config.getoption("browser_name")

    # if browser_name =="chrome":
    #     # service = Service("C:\Work\Project\Chrome\chromedriver_win32_111\chromedriver.exe")
    #     # "C:\Work\Project\Firefox\gecodriver_33\geckodriver.exe"
    #     # driver = webdriver.Chrome(service=service)
    service = "C:\Work\Project\Chrome\chromedriver_win32_113\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=service)
    # elif browser_name =="firefox":
    #     service = Service("C:\Work\Project\Firefox\gecodriver_33\geckodriver.exe")
    #     driver = webdriver.Firefox(executable_path=service)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    # return driver
    request.cls.driver = driver
    yield
    driver.close()

# @pytest.fixture(scope= "class")
# def browserInvoke(request):
#     service = Service("C:\Work\Project\Chrome\chromedriver_win32_111\chromedriver.exe")
#     driver = webdriver.Chrome(service=service)
#     driver.maximize_window()
#     #return driver
#     request.cls.driver = driver
#     yield
#     driver.close()

