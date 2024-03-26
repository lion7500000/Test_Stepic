# //  Amazon_getSign.swift
# //  Created by Liliana Koretska on 3/21/24.
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

AMAZON_LINK = (By.ID, 'twotabsearchtextbox')
EXPECTED = "amazon"
ACTUAL_AMAZON_TEXT = (By.XPATH, "//*[@id='nav-logo']")
#ANOTHER_GMAIL_TEXT_LINK = (By.XPATH, "//*[contains(text(), 'use email')]")
#EXPECTED_AMAZON_TEXT = "Amazon"
AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.XPATH, "//input[@id='twotabsearchtextbox']")
driver.get('https://www.amazon.com/')
sleep(4)
fild = driver.find_element(*AMAZON_LINK)
fild.send_keys('gift')
sleep(4)
# assert EXPECTED in driver.current_url
# assert driver.find_element(*AMAZON_SEARCH_FIELD).send_keys("Amazon")
#assert driver.find_element(*ACTUAL_AMAZON_TEXT).text == EXPECTED

# driver.get('https://amazon.com')
sleep(4)
# driver.find_element(*AMAZON_SEARCH_FIELD).send_keys('gifts for mom', Keys.ENTER)
# #driver.find_element(*AMAZON_SEARCH_FIELD).click()
# sleep(4)