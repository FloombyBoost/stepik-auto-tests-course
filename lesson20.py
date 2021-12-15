from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
         )
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    element_x = browser.find_element_by_id("input_value")
    x = element_x.text
    y = calc(x)
    answer=browser.find_element_by_id("answer")
    answer.send_keys(y)
    button = browser.find_element_by_id("solve")
    button.click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(3)
    