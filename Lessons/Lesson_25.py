import os
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as SF
from selenium.webdriver.chrome.service import Service as SC
driver_path_chrome = SF(os.getcwd() + '/drivers/chromedriver')
driver_path_firefox = SC(os.getcwd() + '/drivers/geckodriver')


driver = webdriver.Firefox(service=driver_path_firefox)
url = 'https://github.com/builuk1/builuk1-QA03/blob/master/bot.py'

driver.get(url)
driver.maximize_window()
url = 'https://test.mensa.no'
driver.get(url)
print(driver.title)

button_18_50 = '/html/body/div[2]/main/cach/div[1]/div/div/div[2]/div/button[2]'
button_51_60 = '/html/body/div[2]/main/cach/div[1]/div/div/div[2]/div/button[3]'
button_start = driver.find_element('xpath', button_18_50)
button_start.click()


#
# driver = webdriver.Firefox(service=driver_path_firefox)
# #driver = webdriver.Chrome(service=driver_path_chrome)
# url = 'https://core.telegram.org/'driver.get(url)
# # driver.set_window_position(1600,300)#Для второго монитора расположенного справа
# time.sleep(2)
# driver.maximize_window()
#HEADLESS БЕЗГОЛОВЫЙ Режим работы без визуального запуска
# driver.set_window_size(300,100)
url = 'https://test.mensa.no/'
driver.get(url)
print(driver.title)
button_18_50_xpath = '/html/body/div[2]/main/cach/div[1]/div/div/div[2]/div/button[2]'
button_51_60_xpath = '/html/body/div[2]/main/cach/div[1]/div/div/div[2]/div/button[3]'
button_51_60 = driver.find_element('xpath',button_51_60_xpath)
print(button_51_60.text)
button_18_50 = driver.find_element('xpath',button_18_50_xpath)
print(button_18_50.text)
time.sleep(2)
button_18_50.click()
button_start_xpath = '//*[@id="startTest"]'
button_start_xpath_full = '/html/body/div[2]/main/cach/div[2]/div/div/div/div[2]/button'
button_start = driver.find_element('xpath',button_start_xpath_full)
time.sleep(2)
button_start.click()

ex1_f_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[6]/div/img'
ex1_f_xpath = driver.find_element('xpath',ex1_f_xpath)
ex1_f_xpath.click()

ex2_c_xpath = '/html/body/div[2]/main/cach/div[3]/div[2]/div[3]/div[3]/div/img'
ex2_c_xpath = driver.find_element('xpath', ex2_c_xpath)
ex2_c_xpath.click()

ex3_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[3]/div[3]/div[1]/div/img'
ex3_a_xpath = driver.find_element('xpath', ex3_a_xpath)
ex3_a_xpath.click()

# ex4_e_xpath = '/html/body/div[2]/main/cach/div[3]/div[4]/div[3]/div[5]/div/img'
# ex4_e_xpath = driver.find_element('xpath', ex4_4_xpath)
# ex4_e_xpath.click()