'''
Работа с помощью Selenium.
Провести тест, с записью результатов.
Можно написать тест любого сайта, на котором есть регистрация и radio button, checkbox Критерии: вход на сайт,
запись полученных результатов, запись выбранных вариантов, проверка на все возможные варианты ответа.
Варианты сайтов: .
'''
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Логирование
import logging
file = "/Users/apple/Downloads/Logs.txt"
try:
    open(file, 'a').close()
except OSError:
    print('Ошибка создания файла')
else:
    print('Лог файл создан')
logging.basicConfig(filename=file, level=logging.INFO, filemode="w")

# logging.debug("This is a debug message")
# logging.info("Informational message")
# logging.error("An error has happened!")



# Функция ожидания элементов
def wait_of_element(xpath, driver):
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    # print(' tag:', element.tag_name)
    # print('text:', element.text)
    return element

#Функция переключения на фрейм
def wait_for_frame(driver):
    wait = WebDriverWait(driver, 30).until(
        EC.frame_to_be_available_and_switch_to_it(0))
    return wait



#1 открываем и разворачиваем окно хрома
logging.info("Старт анализа")
driver_path_chrome = os.getcwd() + '/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path_chrome)
try:
    driver.get('http://automationpractice.com')
    driver.maximize_window()
    logging.info("Страница открыта")
except:
    logging.error("Сбой открытия страницы")
# title = "//head/title[text() = 'My Store']"
# a = driver.find_element(By.XPATH, title)

#2 клик по лого
try:
    sign_in_but = "//a/img[@class='logo img-responsive']"
    wait_of_element(sign_in_but, driver).click()
    logging.info("Клик по лого прошел")
except:
    logging.error("Сбой клика по лого")

#3 нажатие на кнопку sign in
try:
    login_button = "//div/a[@class='login' and @title = 'Log in to your customer account']"
    wait_of_element(login_button, driver).click()
    logging.info("Клик по кнопке Sign in прошел")
except:
    logging.error("Сбой клика по кнопке Sign in")
#
#
#
# #4 ввод логина
try:
    log_email_address = "//input[@name='email' and @id='email']"
    authorization = driver.find_element(By.XPATH, log_email_address)
    authorization.send_keys("text@mail.com")
    logging.info("Ввод логина прошел")
except:
    logging.error("Ввод логина не отработал")

#5 ввод пароля
try:
    log_password = "//input[@name='passwd' and @id='passwd']"
    authorization = driver.find_element(By.XPATH, log_password)
    authorization.send_keys("123456789")
    logging.info("Ввод пароля прошел")
except:
    logging.error("Ввод пароля не отработал")

#6 Нажатие кнопки авторизации
try:
    submit_login_button = "//button[@type='submit'  and @id='SubmitLogin']"
    wait_of_element(submit_login_button, driver).click()
    logging.info("Попытка авторизация прошла")
except:
    logging.error("Попытка авторизация не прошла")

# Проверка авторизации
if driver.find_element(By.XPATH, "//div[@class='row']/div[@id='center_column']/div[@class='alert alert-danger']/ol/li")\
        .text == "Invalid email address":
    logging.error("Invalid email address")
elif driver.find_element(By.XPATH, "//div[@class='row']/div[@id='center_column']/div[@class='alert alert-danger']/ol/li")\
        .text == "An email address required.":
    logging.error("An email address required")
elif driver.find_element(By.XPATH, "//div[@class='row']/div[@id='center_column']/div[@class='alert alert-danger']/ol/li")\
        .text == "Authentication failed.":
    logging.error("Authentication failed")
else:
    logging.info("Успешный вход")

#7 клик по лого
try:
    sign_in_but = "//a/img[@class='logo img-responsive']"
    wait_of_element(sign_in_but, driver).click()
    logging.info("Клик по лого прошел")
except:
    logging.error("Сбой клика по лого")

#8 переход по ссылке woman
try:
    women_button = "//a[text()='Women']"
    wait_of_element(women_button, driver).click()
    logging.info("Переход по кнопке Woman")
except:
    logging.error("Сбой перехода по кнопке Woman")


#9 клик по фильтру черный цвет
try:
    check_box_black_color = "//input[@class='color-option  ' and @style='background: #434A54;']"
    wait_of_element(check_box_black_color, driver).click()
    logging.info("Клик по чек боксу")
except:
    logging.error("Сбой клика по чек боксу")


#10 Клик по картинке Blouse
try:
    # blouse = "//img[@alt='Blouse']"
    blouse = "//a[@class='product_img_link' and @title='Blouse']/img"
    wait_of_element(blouse, driver).click()
    logging.info("Клик по картинке Blouse")
except:
    logging.error("Сбой клика по картинке Blouse")


#11 Перехват всплывающего окна
try:
    wait_for_frame(driver)
    logging.info("Перехват всплывающего окна")
except:
    logging.error("Сбой перехвата всплывающего окна")


#12 Клик адд ту карт
try:
    click_addcart = "//button[@type='submit' and @name='Submit']/span"
    wait_of_element(click_addcart, driver).click()
    time.sleep(3)
    logging.info("Клик адд ту карт")
except:
    logging.error("Сбой клика адд ту карт")


# 13 Возврат на главную страницу
try:
    driver.get('http://automationpractice.com')
    logging.info("Страница открыта")
except:
    logging.error("Сбой открытия страницы")

#14 переход по ссылке woman
try:
    women_button = "//a[text()='Women']"
    wait_of_element(women_button, driver).click()
    logging.info("Переход по кнопке Woman")
except:
    logging.error("Сбой перехода по кнопке Woman")

#15 Клик по кнопке цвета товара
try:
    click_color = "//div[@class='right-block']/div/ul[@class = 'color_to_pick_list clearfix']/li/a[@id='color_1']"
    wait_of_element(click_color, driver).click()
    logging.info("Переход по кнопке цвета товара")
except:
    logging.error("Сбой перехода по кнопке цвета товара")


#16 Переход на страницу с radio button
try:
    driver.get('http://automationpractice.com/index.php?id_product=1&controller=product#/size-s/color-orange')
    logging.info("Переход успешен")
except:
    logging.error("Переход не произошел")

#17 проверка выбора radio button
try:
    color1_radio_button = "//ul[@id = 'color_to_pick_list']/li/a[@id='color_13']"
    wait_of_element(color1_radio_button, driver).click()
    logging.info("Переход по radio button цвета товара")
except:
    logging.error("Сбой перехода по radio button цвета товара")

select1_radio_button = "//ul[@id = 'color_to_pick_list']/li/a[@id='color_13' and @class = 'color_pick selected']"
select2_radio_button = "//ul[@id = 'color_to_pick_list']/li/a[@id='color_14' and @class = 'color_pick selected']"
color1_radio_button =  "//ul[@id = 'color_to_pick_list']/li/a[@id='color_13' and @class = 'color_pick']"
color2_radio_button =  "//ul[@id = 'color_to_pick_list']/li/a[@id='color_14' and @class = 'color_pick']"
if driver.find_element(By.XPATH, select1_radio_button) and driver.find_element(By.XPATH, color2_radio_button):
    logging.info("Переход по radio button прошел корректно")
else:
    logging.error("Переход по radio button прошел не корректно")

#18 Переход в корзину и очищаем ее
try:
    driver.get('http://automationpractice.com/index.php?controller=order')
    clear_cart = "//a[@class='cart_quantity_delete' and @title='Delete']"
    wait_of_element(clear_cart, driver).click()
    time.sleep(3)
    logging.info("Переход в корзину и ее очистка")
except:
    logging.error("Сбой очистки корзины")

# 19 Окончание теста и закрытие браузера драйвером
driver.close()
