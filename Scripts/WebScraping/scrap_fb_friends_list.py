#!/usr/bin/env python
# coding: utf-8

# In[146]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import getpass

PATH = "C:\Program Files\drivers\chromedriver_103.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.facebook.com/")
driver.maximize_window()


# In[117]:


loginId = "yourLogInIDhere"


# In[118]:


my_password = getpass.getpass()


# In[119]:


user_name = driver.find_element(By.XPATH,"//input[@type='text']")
user_name.send_keys("smrvrma16@gmail.com")

password = driver.find_element(By.XPATH,"//input[@placeholder='Password']")
password.send_keys(my_password)


# In[120]:


log_in_button = driver.find_element(By.XPATH,"//button[@type='submit']")
log_in_button.click()


# In[121]:


my_profile = driver.find_element(By.XPATH,"//span[text()='Sameer Verma']")
my_profile.click()
sleep(3)


# In[129]:


friendsTab = driver.find_element(By.XPATH,"//span[text()='Friends']")
friendsTab.click()
sleep(3)


# In[130]:


friendsList = set()

my_friend = driver.find_elements(By.XPATH,"//div[@class='buofh1pr hv4rvrfc']")
while True:
    for friend in my_friend:
        friendsList.add(friend.text)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(10)
    my_friend = driver.find_elements(By.XPATH,"//div[@class='buofh1pr hv4rvrfc']")
    if len(set(friendsList)) > 400:
        break


# In[142]:


len(friendsList)


# In[143]:


import pandas as pd


# In[144]:


df = pd.DataFrame(friendsList,columns=['names'])

# df.head()

df_new[['name','count']] = df['names'].str.split("\n",expand=True)
df_final = df_new[['name','count']]
df_final.shape


# In[145]:


df.shape

