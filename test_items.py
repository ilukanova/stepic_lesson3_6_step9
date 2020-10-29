from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


def test_if_button_add_to_basket_exist(browser):
    browser.get(link)
    button = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert button, 'Button is not found'

