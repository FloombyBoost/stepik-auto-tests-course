from selenium import webdriver
import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1=browser.find_element_by_name("firstname")
    input1.send_keys("G")
    input2=browser.find_element_by_name("lastname")
    input2.send_keys("B")
    input3=browser.find_element_by_name("email")
    input3.send_keys("@")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    element=browser.find_element_by_name("file")
    #element.send_keys(file_path)
    print(current_dir) #покажет вам дирректорию, в которой у вас лежит ваш исполняемый код
    print(file_path)  #путь до вашего файла который вы хотите загрузить
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()