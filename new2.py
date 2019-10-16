from selenium import webdriver
import time 
# Чтобы убедиться, что возникает ошибка, необходимо поменять цифру "1" в конце ссылки на "2"
link = "http://suninjuly.github.io/registration1.html"


try:

    browser = webdriver.Chrome() #Открываем браузер 
    browser.get(link) #Открываем ссылку

    input1 = browser.find_element_by_xpath('//label[text()="First name*"]/following-sibling::input')
    input1.send_keys("Ivan") #Вводим имя
    input2 = browser.find_element_by_xpath('//label[text()="Last name*"]/following-sibling::input')
    input2.send_keys("Ivanov") # Вводим фамилию
    input3 = browser.find_element_by_xpath('//input[@class="form-control third"]')
    input3.send_keys("Petrov@ivan.ru") #Вводим почту
    input4 = browser.find_element_by_xpath('//label[text()="Phone:"]/following-sibling::input')
    input4.send_keys("89122131231") #Вводим номер телефона
    input5 = browser.find_element_by_xpath('//label[text()="Address:"]/following-sibling::input')
    input5.send_keys("Russia") #Вводим адрес
    button = browser.find_element_by_xpath('//button[@class="btn btn-default"]')
    button.click() #Нажимаем на кнопку
    time.sleep(1) #Ждем загрузки страницы

    welcome_text_elt = browser.find_element_by_tag_name("h1")  # находим элемент, содержащий текст
    
    welcome_text = welcome_text_elt.text # записываем в переменную welcome_text текст из элемента welcome_text_elt

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла