import time
link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_cart_button_present(browser):
    browser.get(link)
    time.sleep(30)
    add_to_basket = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert add_to_basket, 'Button add to cart is not present'