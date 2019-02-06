from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
driver.get("https://vtop.vit.ac.in/vtop")
Submit=driver.findElement(By.cssSelector("button[type='submit']"));
Submit.click()
