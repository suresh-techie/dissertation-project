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

import os
print(os.environ['BUILD_NUMBER'])

def test1_open_browser_url():
    print("TEST NAME: test1_open_browser_url")
    text_box = "ta"
    driver = webdriver.Chrome()
    driver.get("https://omayo.blogspot.com/")
    driver.maximize_window()
    time.sleep(10)
    try:
        element = driver.find_element(By.ID, text_box)
        element.send_keys("This is for testing..")
    except Exception as err:
        raise Exception("RuntimeError no such element Unable to locate element")
    time.sleep(10)
