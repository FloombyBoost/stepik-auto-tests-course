from selenium import webdriver
import math
import time
link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(2)
    element_x = browser.find_element_by_id("input_value")
    x = element_x.text
    y = calc(x)
    answer=browser.find_element_by_id("answer")
    answer.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(3)
    browser.quit()