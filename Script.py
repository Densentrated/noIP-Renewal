import Constants, os, selenium, time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(ChromeDriverManager().install())
noIPWebsite = browser.get(Constants.WEBSITEURL)

noIPWebsite.find_element(By.XPATH, '//*[@id="email"]').send_keys(Constants.USERNAME)
