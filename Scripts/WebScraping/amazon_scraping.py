import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files\drivers\chromedriver_103.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.amazon.in")
driver.maximize_window()

search_box = driver.find_element(By.ID,"twotabsearchtextbox")
search_box.clear()
search_box.send_keys("dell laptops")
driver.find_element(By.ID,"nav-search-submit-button").click()
driver.find_element(By.XPATH,"//span[text()='Dell']").click()

laptops = driver.find_elements(By.XPATH,'//div[@data-component-type="s-search-result"]')

laptop_name = []
laptop_price = []
no_reviews = []
final_list = []

for laptop in laptops: 
  
    names =laptop.find_elements(By.XPATH,".//span[@class='a-size-medium a-color-base a-text-normal']")
    for name in names:
        laptop_name.append(name.text)
        
    try:
        if len(laptop.find_elements(By.XPATH,".//span[@class='a-price-whole']"))>0:
            prices= laptop.find_elements(By.XPATH,".//span[@class='a-price-whole']")
            for price in prices:
                # print('the lenght is ===>',len(price.text))
                laptop_price.append(price.text)
        else:
            laptop_price.append("0")
    except:
        pass
    # reviews = laptop.find_elements(By.XPATH,".//span[@class='a-size-base s-underline-text']")
    
    try:
        if len(laptop.find_elements(By.XPATH,".//span[@class='a-size-base s-underline-text']"))>0:
            reviews = laptop.find_elements(By.XPATH,".//span[@class='a-size-base s-underline-text']")
            for review in reviews:
                # print('the length is===>', len(review.text), review.text)
                no_reviews.append(review.text)
        else:
            no_reviews.append("0")
    except:
        pass
        
print('no of laptops==>',len(laptop_name))
print('no of prices==>',len(laptop_price))
print('no of reviews==>',len(no_reviews))


import pandas as pd
df = pd.DataFrame(zip(laptop_name,laptop_price,no_reviews),columns=['laptop_name','laptop_price','no_reviews'])

df.to_excel(r"D:\Learnerea\Tables\laptops.xlsx",index=False)

driver.quit()

