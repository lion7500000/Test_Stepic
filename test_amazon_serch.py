import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
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
    search_btn = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(SUBMIT_BTN))
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


def test_sin_in_back(browser):
    SIGN_IN_POPUP = (By.CSS_SELECTOR, "div#nav-signin-tooltip span.nav-action-inner")
    SIGN_IN_TEXT = (By.CSS_SELECTOR, "div[class *= 'extra-large'] h1")
    EXPECTED_SIGN_TEXT = "Sign in"
    AMAZON_ALL_MAIN_PAIGE = (By.CSS_SELECTOR, "div#nav-main div.nav-left")

    browser.get(amazon_base)
    wait = WebDriverWait(browser, 5)
    wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP)).click()

    # print(browser.find_element(*SIGN_IN_TEXT).text)
    # print(wait.until(EC.text_to_be_present_in_element(SIGN_IN_TEXT, EXPECTED_SIGN_TEXT)))
    assert EXPECTED_SIGN_TEXT == browser.find_element(*SIGN_IN_TEXT).text, f"{EXPECTED_SIGN_TEXT} is not present"

    browser.back()
    assert browser.find_element(*AMAZON_ALL_MAIN_PAIGE).text == "All"

@pytest.mark.xfail
def test_size_chose(browser):
    AMAZON_SEARCH_BAR = (By.CSS_SELECTOR, "div.nav-fill input[id *= 'box']")
    SEARCH_WORD = "Nike for mike"
    LIST_OF_ITEMS = (By.XPATH, "//div[contains(@class, 'right-micro')]")
    SELECT_SIZE = (By.CSS_SELECTOR, "#productTitle")
    # CILICK = (By.CSS_SELECTOR, "a#native_dropdown_selected_size_name_12")

    browser.get(amazon_base)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located(AMAZON_SEARCH_BAR)).send_keys(SEARCH_WORD, Keys.ENTER)

    search_text = wait.until(EC.visibility_of_all_elements_located(LIST_OF_ITEMS))

    for item in search_text:
        try:
            actual_text = item.text.split()

            if 'Nike' in actual_text:
                item.click()
        except:
            break

    chose_item_text = wait.until(EC.visibility_of_element_located(SELECT_SIZE)).text
    assert "Nike" in chose_item_text, f"{chose_item_text} not found"


