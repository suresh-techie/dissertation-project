from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import logging

# text_box = "ta1"
# text_box = "ta"

# driver = webdriver.Chrome()
# driver.get("https://omayo.blogspot.com/")
# driver.maximize_window()
# # driver.implicitly_wait(10)
# import time
# time.sleep(10)
# driver.find_element(By.ID, text_box).send_keys("testing..")
# time.sleep(10)

import os
print(os.environ['BUILD_NUMBER'])

def test1_open_browser_url():
    text_box = "ta"
    driver = webdriver.Chrome()
    driver.get("https://omayo.blogspot.com/")
    driver.maximize_window()
    # driver.implicitly_wait(10)
    time.sleep(10)
    driver.find_element(By.ID, text_box).send_keys("This is for testing..")
    time.sleep(10)
