import Constants
import selenium
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


#sets some browser options
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

#gets browser and opens website
browser = webdriver.Chrome(ChromeDriverManager().install(), options = options)
browser.get(Constants.WEBSITEURL)

# gets through the login page
# page elements
emailBox = browser.find_element(By.XPATH, "/html/body/section[3]/section/div/div/div/div/div/div[2]/form/section[1]/input")
passwordBox = browser.find_element(By.XPATH, "/html/body/section[3]/section/div/div/div/div/div/div[2]/form/section[2]/input")
loginButton = browser.find_element(By.XPATH, "/html/body/section[3]/section/div/div/div/div/div/div[2]/form/button")

if emailBox != None and passwordBox != None:
    print("Found email and password boxes, entering info...")

emailBox.send_keys(Constants.USERNAME)
passwordBox.send_keys(Constants.USERPASSWORD)
loginButton.click()

# gets to hostname menu
time.sleep(2)
browser.get("https://my.noip.com/dynamic-dns?mode=edit&id=84780181")

#clicks cancel button
time.sleep(1)
cancelButton = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[4]/div/div/div/div[4]/button[2]")
cancelButton.click()
# clicks confirm button
time.sleep(1)
confirmButton = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/div[2]/div/div/div[2]/div[1]/table/tbody/tr/td[5]/button[1]")
confirmButton.click()

print ("IP Renewed!")
browser.close()

