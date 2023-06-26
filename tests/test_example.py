from selenium.webdriver.common.by import By


def test_main_page_elements(browser):
    '''Проверка элементов на главной странице магазина'''
    browser.get(browser.url)
    browser.find_element(By.ID, "search")
    browser.find_element(By.CSS_SELECTOR, "button[type='button']")
    browser.find_element(By.XPATH, "//*[text()='Desktops']")
    browser.find_element(By.LINK_TEXT, "Canon EOS 5D")
    browser.find_element(By.LINK_TEXT, "About Us")


def test_catalog(browser):
    '''Проверка элементов в каталоге товаров Cameras'''
    browser.get(browser.url + "/camera")
    browser.find_element(By.CLASS_NAME, "fa-home")
    browser.find_element(By.ID, "cart-total")
    browser.find_element(By.ID, "input-sort")
    browser.find_element(By.ID, "input-limit")
    browser.find_element(By.LINK_TEXT, "Nikon D300")


def test_product(browser):
    '''Проверка элементов в карточке товара Macbook'''
    browser.get(browser.url + "/macbook")
    browser.find_element(By.LINK_TEXT, "Apple")
    browser.find_element(By.CLASS_NAME, "tab-content")
    browser.find_element(By.CLASS_NAME, "tab-content")
    browser.find_element(By.LINK_TEXT, "Write a review")
    browser.find_element(By.LINK_TEXT, "Specification")


def test_admin_page_elements(browser):
    '''Проверка элементов на странице логина в админку'''
    browser.get(browser.url + "/admin") 
    browser.find_element(By.ID, "input-username")
    browser.find_element(By.NAME, "password")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.find_element(By.LINK_TEXT, "Forgotten Password")
    browser.find_element(By.XPATH, "//*[text()='OpenCart']")


def test_registration_page(browser):
    '''Проверка элементов на странице регистрации пользователя'''
    browser.get(browser.url + "/index.php?route=account/register")
    browser.find_element(By.ID, "content")
    browser.find_element(By.LINK_TEXT, "login page")
    browser.find_element(By.LINK_TEXT, "Privacy Policy")
    browser.find_element(By.XPATH, "//*[text()='OpenCart']")
    browser.find_element(By.XPATH, "//*[text()='Your Personal Details']")