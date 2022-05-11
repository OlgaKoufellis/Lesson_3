'''
Работа с помощью Selenium.
Провести тест, с записью результатов.
Можно написать тест любого сайта, на котором есть регистрация и radio button, checkbox Критерии: вход на сайт,
запись полученных результатов, запись выбранных вариантов, проверка на все возможные варианты ответа.
Варианты сайтов: .

https://replit.com/
https://myshows.me/

'''

import os
# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Функция ожидания элементов
def wait_of_element(xpath, driver):
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    print(' tag:', element.tag_name)
    print('text:', element.text)
    return element

#Функция переключения на фрейм
def wait_for_frame(driver):
    WebDriverWait(driver, 30).until(
        EC.frame_to_be_available_and_switch_to_it(0)
    )


driver_path_chrome = os.getcwd() + '/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path_chrome)

# Open site
driver.get('http://automationpractice.com')
driver.maximize_window()
# wait = WebDriverWait(driver, 20)

title = "//head/title[text() = 'My Store']"
a = driver.find_element(By.XPATH, title)
print(a)


logo = "//a/img[@class='logo img-responsive']"
logo_go = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
logo_go.click()


login_button = "//div/a[@class='login' and @title = 'Log in to your customer account']"
login_but = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, login_button)
    )
)
login_but.click()


log_email_address = "//input[@name='email' and @id='email']"
authorization = driver.find_element(By.XPATH, log_email_address)
# if authorization:
#     print(True)
# else:
#     print(False)

authorization.send_keys("text@mail.com")



log_password = "//input[@name='passwd' and @id='passwd']"
authorization = driver.find_element(By.XPATH, log_password)
# if authorization:
#     print(True)
# else:
#     print(False)

authorization.send_keys("123456789")


submit_login_button = "//button[@type='submit'  and @id='SubmitLogin']"
driver.find_element(By.XPATH, submit_login_button)
submit_login_but = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, submit_login_button)
    )
)
submit_login_but.click()


logo = "//a/img[@class='logo img-responsive']"
logo_go = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
logo_go.click()



women_button = "//a[text()='Women']"
driver.find_element(By.XPATH, women_button)
women_but = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, women_button)
    )
)
women_but.click()


check_box_black_color = "//input[@class='color-option  ' and @style='background: #434A54;']"
driver.find_element(By.XPATH, check_box_black_color)
check_box_black_colour = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, check_box_black_color)
    )
)
check_box_black_colour.click()


blouse = "//img[@alt='Blouse']"
driver.find_element(By.XPATH, blouse)
blous = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, blouse)
    )
)
blous.click()


#11 Перехват всплывающего окна
wait_for_frame(driver)

#12 Клик адд ту карт
click_addcart = "//button[@type='submit' and @name='Submit']/span"
wait_of_element(click_addcart, driver).click()


# xf = driver.find_element(By.XPATH('//*[@class="if"]'))
# driver.switch_to.frame(xf)

# proceed_to_checkout = "//a[@title='Proceed to checkout']"
# wait_of_element(proceed_to_checkout, driver).click()




# driver.close()