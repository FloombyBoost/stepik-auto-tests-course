from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    element_x=browser.find_element_by_id("input_value")
    x=element_x.text
    y=calc(x)
    element_answer=browser.find_element_by_id("answer")
    element_answer.send_keys(y)
    element_check=browser.find_element_by_id("robotCheckbox") 
    element_check.click()
    element_rule=browser.find_element_by_id("robotsRule") 
    element_rule.click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()