from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MENU = (By.CSS_SELECTOR, 'div.bm-burger-button')
ABOUT = (By.ID, 'about_sidebar_link')
ABOUT_TEXT = (By.CSS_SELECTOR, "h1.MuiTypography-root.MuiTypography-h1.css-odgtd8")
RESET_APP = (By.CSS_SELECTOR, 'a[data-test="reset-sidebar-link"]')
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
CART_BADGE_WITH_ITEM = (By.CSS_SELECTOR, "span.shopping_cart_badge")
CART_BADGE_EMPTY = (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")

from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
browser = webdriver.Chrome(service=service)
browser.maximize_window()
browser.implicitly_wait(5)
wait = WebDriverWait(browser, 20)


def test_auth_positive():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'url не соответствует ожидаемому'


""""
def test_auth_negative():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('problem_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    browser.find_element(By.XPATH, '//h3[@data-test="error"]')
"""


# Добавление товара в корзину через каталог
def test_auth_add_product_to_cart_from_catalog():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    add_to_cart_button = browser.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button")
    add_to_cart_button.click()


#         Удаление товара из корзины через корзину
def test_auth_remove_product_from_cart():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    add_to_cart_button = browser.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button")
    add_to_cart_button.click()
    remove_button = browser.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button")
    remove_button.click()


def test_auth_add_product_to_cart_from_product_page():
    login()
    add_to_cart_button = browser.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button")
    add_to_cart_button.click()
    remove_button = browser.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button")
    remove_button.click()
    backpack_card = browser.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
    backpack_card.click()
    add = browser.find_element(By.XPATH, "//*[@id='inventory_item_container']/div/div/div/button")
    add.click()


def login():
    browser.get('https://www.saucedemo.com/')
    browser.implicitly_wait(10)
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()


def test_auth_add_from_card():
    login()
    product_card = browser.find_element(By.XPATH, '//*[@id="item_4_img_link"]/img').click()


"""
def placing_order()
    login()
    add_to_cart_button = browser.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[3]/button")
    add_to_cart_button.click()
"""


# Фильтр
#
# Проверка работоспособности фильтра (A to Z)
# Проверка работоспособности фильтра (Z to A)
# Проверка работоспособности фильтра (low to high)
# Проверка работоспособности фильтра (high to low)

def test_auth_sorted_prices():
    login()
    sorted_prices_1 = browser.find_element(By.XPATH, '//option[@value="az"]').click()
    sorted_prices_2 = browser.find_element(By.XPATH, '//option[@value="za"]').click()
    sorted_prices_3 = browser.find_element(By.XPATH,
                                           '//select[@class="product_sort_container"]/option[@value="lohi"]').click()
    sorted_prices_4 = browser.find_element(By.XPATH,
                                           '//select[@class="product_sort_container"]/option[@value="hilo"]').click()


# Бургер меню
#
# Выход из системы
# Проверка работоспособности кнопки "About" в меню
# Проверка работоспособности кнопки "Reset App State"


def burger_menu():
    login()
    wait.until(EC.element_to_be_clickable(MENU)).click()


def test_about():
    burger_menu()
    wait.until(EC.element_to_be_clickable(ABOUT)).click()
    text_about = wait.until(EC.visibility_of_element_located(ABOUT_TEXT)).text
    assert "Web" in text_about, f"expected result 'Website' bot got {text_about}"


def test_reset_app():
    login()
    wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN)).click()
    basket_before = wait.until(EC.visibility_of_element_located(CART_BADGE_WITH_ITEM)).text
    assert basket_before == '1', f"expected result '1', bot got {basket_before}"
    wait.until(EC.element_to_be_clickable(MENU)).click()
    wait.until(EC.element_to_be_clickable(RESET_APP)).click()
    assert wait.until(EC.invisibility_of_element_located(CART_BADGE_WITH_ITEM)) == True
    basket_after = wait.until(EC.visibility_of_element_located(CART_BADGE_EMPTY)).text
    assert basket_after == ''


