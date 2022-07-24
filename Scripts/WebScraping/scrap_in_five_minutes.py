import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PATH = "C:\Program Files\drivers\chromedriver_103.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.amazon.in/s?k=python+books&crid=2WB4NZD0EQNGG&sprefix=python+books%2Caps%2C251&ref=nb_sb_noss_1")
driver.maximize_window()


books = []

book = driver.find_elements(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")

for x in book:
    books.append(x.text)
    
len(books)
print(books)