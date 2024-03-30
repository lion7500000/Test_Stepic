from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(5)

BASE_URL = "https://www.amazon.com/"
SIGN_IN_POPUP = (By.CSS_SELECTOR, "div#nav-signin-tooltip span.nav-action-inner")
SIGN_IN_TEXT = (By.CSS_SELECTOR, "div[class *= 'extra-large'] h1")
EXPECTED_SIGN_TEXT = "Sign in"
AMAZON_ALL_MAIN_PAIGE = (By.CSS_SELECTOR, "div#nav-main div.nav-left")
AMAZON_SEARCH_BAR = (By.CSS_SELECTOR, "div.nav-fill input[id *= 'box']")
SEARCH_WORD = "shoes for mike"
LIST_OF_ITEMS = (By.XPATH, "//div[contains(@class, 'right-micro')]")
SELECT_SIZE = (By.CSS_SELECTOR, "span#dropdown_selected_size_name span.a-button-text.a-declarative")
CILICK = (By.CSS_SELECTOR, "a#native_dropdown_selected_size_name_12")

driver.get(BASE_URL)
sleep(4)
wait = WebDriverWait(driver, 5)
wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP)).click()

print(driver.find_element(*SIGN_IN_TEXT).text)
print(wait.until(EC.text_to_be_present_in_element(SIGN_IN_TEXT, EXPECTED_SIGN_TEXT)))
assert EXPECTED_SIGN_TEXT == driver.find_element(*SIGN_IN_TEXT).text, f"{EXPECTED_SIGN_TEXT} is not present"

driver.back()
assert driver.find_element(*AMAZON_ALL_MAIN_PAIGE).text == "All"

driver.find_element(*AMAZON_SEARCH_BAR).send_keys(SEARCH_WORD, Keys.ENTER)

a = driver.find_elements(*LIST_OF_ITEMS) # -- > list
x = True

for char in a:
    try:
        actual = char.text.split()
        print(char)
        print(actual)
        if "Nike" in actual:
            #wait.until(EC.element_to_be_clickable(char)).click()
            char.click()
            sleep(3)
    except:
        break

driver.find_element(*SELECT_SIZE).click()
wait.until(EC.element_to_be_clickable(CILICK)).click()
sleep(3)