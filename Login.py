import time                                                                                                                        
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.get("https://vtop.vit.ac.in/vtop")
submit=driver.find_elements_by_xpath("//button[contains(text(),'Login to V-TOP')]")[0]
submit.click()
time.sleep(2)
username=driver.find_element_by_css_selector("#uname")
username.send_keys("18BCE3212")
password=driver.find_element_by_css_selector("#passwd")
password.send_keys("asdfklsdf")
time.sleep(4)
driver.find_elements_by_xpath("//button[contains(text(),'Sign in')]")[0].click()
