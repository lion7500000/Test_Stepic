from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

amazon_base = 'https://www.amazon.com/'
AMAZON_SEARCH_FILD = (By.ID, 'twotabsearchtextbox')
INPUT_TEXT = 'Printer'
SEARCH_TEXT = (By.XPATH, '//span[@class="a-color-state a-text-bold"]')
SUBMIT_BTN = (By.ID, 'nav-search-submit-button')
SEARCH_RESULTS = (By.XPATH, '//span[@class="a-size-medium a-color-base a-text-normal"]')
SEARCH_TITLE = (By.ID, 'title')


def test_search_fild(browser):
    browser.get(amazon_base)
    browser.find_element(*AMAZON_SEARCH_FILD).send_keys(INPUT_TEXT)
    search_btn = WebDriverWait(browser,5).until(EC.element_to_be_clickable(SUBMIT_BTN))
    search_btn.click()
    actual_text = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SEARCH_TEXT)).text
    assert INPUT_TEXT in actual_text, f"expected text {INPUT_TEXT}, bot got {actual_text}"
    item = browser.find_elements(*SEARCH_RESULTS)[4]
    item_text = item.text
    item.click()
    title_of_item = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(SEARCH_TITLE)).text
    new_window = browser.current_url
    assert amazon_base in new_window
    # assert item_text == title_of_item
    WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element(SEARCH_TITLE, item_text))




