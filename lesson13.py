from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

link = "  http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    element_x1=browser.find_element_by_id("num1")
    element_x2=browser.find_element_by_id("num2")
    x1=element_x1.text
    x2=element_x2.text
    y=int(x1)+int(x2)
    print(y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(y)) # ищем элемент с текстом "Python"
    
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