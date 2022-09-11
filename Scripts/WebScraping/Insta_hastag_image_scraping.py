#!/usr/bin/env python
# coding: utf-8

# In[9]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import getpass


# In[10]:


my_user = "smrvrma16@gmail.com"
my_pwd = getpass.getpass()


# In[ ]:


dest_loc = r'D:\Learnerea\notes_scripts\python\webScrapping\outputs\instagram_photos'


# In[11]:


PATH = "C:\Program Files\drivers\chromedriver_105.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")
driver.maximize_window()
sleep(3)


# In[12]:


user_name = driver.find_element(By.XPATH,"//input[@name='username']")
user_name.send_keys(my_user)
user_name.send_keys(Keys.ENTER)


# In[13]:


password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys(my_pwd)
password.send_keys(Keys.ENTER)
sleep(3)


# In[15]:


not_now = driver.find_element(By.XPATH,"//button[text()='Not Now']")
not_now.click()


# In[19]:


search_box = driver.find_element(By.XPATH,"//input[@aria-label='Search input']")
search_box.clear()
search_box.send_keys("#learnerea")


# In[21]:


search_box.send_keys(Keys.ENTER)


# In[22]:


images = driver.find_elements(By.XPATH,"//img[@class='_aagt']")


# In[31]:


my_images = set()

while True:
    for image in images:
        source = image.get_attribute('src')
        my_images.add(source)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(3)
    images = driver.find_elements(By.XPATH,"//img[@class='_aagt']")
    if len(my_images)>10:
        break


# In[32]:


import wget

for image in my_images:
    wget.download(image,dest_loc)

