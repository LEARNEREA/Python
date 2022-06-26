

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files\drivers\chromedriver_103.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.amazon.in")

driver.maximize_window()
driver.minimize_window()
driver.maximize_window()

driver.set_window_size(700, 1000)

search_box = driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')

search_box.send_keys("hp laptops")

driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]').click()


search_box = driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
search_box.clear()
search_box.send_keys("del laptops")
driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]').click()

driver.back()
driver.forward()

