from selenium import webdriver
from selenium.webdriver.chrome.service import Service
def browserInvoke__():
    service = Service("C:\Work\Project\Chrome\chromedriver_win32_111\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver