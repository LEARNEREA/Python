import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PATH = "C:\Program Files\drivers\chromedriver_103.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.rottentomatoes.com/")
driver.maximize_window()


movies_list = ["'War'","'Super 30'","'Agneepath'","'Mohenjo Daro'","'Guzaarish'","'Bang Bang'"]
movie_names = []
audience_counts = []
audience_scores = []
tomatometers = []
movie_infos = []

# subject = "'War'"

for subject in movies_list:
    
    search_path = "//a[contains(text()," +subject+ ")]"
    
    search_box = driver.find_element(By.XPATH,"//input[@slot='search-input']")
    search_box.send_keys(subject)
    search_box.send_keys(Keys.ENTER)
    sleep(3)
    
    movies_tab = driver.find_element(By.XPATH,"//span[contains(text(),'Movies')]")
    movies_tab.click()
    sleep(3)
    
    my_movie = driver.find_element(By.XPATH,search_path)
    movie_name = my_movie.text
    movie_names.append(movie_name)
    my_movie.click()
    sleep(3)
    
    audience_count = driver.find_element(By.XPATH,"//a[@slot='audience-count']").text
    audience_counts.append(audience_count)
    
    
    audience_score = driver.find_element(By.XPATH,"//score-board").get_attribute('audiencescore')
    audience_scores.append(audience_score )
    
    tomatometer = driver.find_element(By.XPATH,"//score-board").get_attribute('tomatometerscore')
    tomatometers.append(tomatometer )
    
    movie_info = driver.find_element(By.XPATH,"//ul[@class='content-meta info']").text.split('\n')
    movie_infos.append(movie_info)
    print(subject," successful")
    sleep(3)
    

import pandas as pd
df = pd.DataFrame(zip(movie_names,audience_counts,audience_scores,tomatometers,movie_infos)
                  ,columns=['movie_names','audience_counts','audience_scores','tomatometers','movie_infos'])

df.to_excel(r"D:\Learnerea\Tables\movie2.xlsx")    
    
    
    
    
    
