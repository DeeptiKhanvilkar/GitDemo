import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get("https://www.amrock.com/company/family")

driver.get_screenshot_as_file("homescreen.png")

introTxt = driver.find_element(By.XPATH, "//div[@class='center-div']/p").text
print(introTxt)

sectionText = driver.find_element(By.XPATH, "//div[@class='section']").text
print(sectionText)

sidePText = driver.find_element(By.XPATH, "//div[@id='w-node-d7f623ec-5fea-8285-8a71-1ed1f03f8ee6-e927f69c']").text
print(sidePText)

homPge = driver.find_element(By.XPATH,"//div[@class='grid-img-div foc']")
assert homPge.is_displayed()

b0ttonText = driver.find_element(By.XPATH,"//div[@class='center-div no-bottom-margin']").text
print(b0ttonText)

action = ActionChains(driver)
menu = driver.find_element(By.XPATH,"//div[@class='main-nav-dropdown']")
action.move_to_element(menu).perform()
action.move_to_element(driver.find_element(By.XPATH,"//*[@id='w-dropdown-list-0']/a[1]")).click().perform()

time.sleep(3)
driver.get_screenshot_as_file("l&B.png")

lbPTxt = driver.find_element(By.XPATH,"//div[@class='section']").text
print(lbPTxt)

time.sleep(3)
amRS_button = driver.find_element(By.XPATH,"//div[@class='fullspan-img team-members']/div/a").click()
childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)
print(driver.find_element(By.XPATH,"//h1[@class='heading-3']").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
# assert "open new window" == driver.find_element_by_xpath("//h1[@class='heading-3']").text