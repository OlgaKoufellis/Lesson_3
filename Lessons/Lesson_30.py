import os
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path_chrome = os.getcwd() + '/drivers/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path_chrome)

# 1 task
driver.get('https://www.yanigen.com.ua')
driver.maximize_window()

#2 task
home_ru = "//a[contain(text(),'ГЛАВНАЯ')]"
# home_ru_button = driver.find_element('xpath',home_ru)
home_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, home_ru)
    )
)
home_ru_button.click()

#3 task
product_ru = "//a[contain(text(ИЗДЕЛИЯ НА ЗАКАЗ)']"
# home_ru_button = driver.find_element('xpath',home_ru)
home_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, product_ru)
    )
)
product_ru_button.click()


''' for Windows

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from xpath import home_page 

    # 1
    driver = webdriver.Chrome()
    driver.get('http://yanigen.com.ua/ru/productstoorder')
    driver.maximize_window() '''
# 2
home_ru = "//ul[@class='menumain']/li/a[@href='/ru/']"

# home_ru_button = driver.find_element('xpath',home_page.home_ru)
home_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, home_page.home_ru)
    )
)
home_ru_button.click()
product_ru = "//ul[@class='menumain']/li/a[@href='/ru/productstoorder']"
# product_ru_button = driver.find_element('xpath',product_ru_ru)
product_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, product_ru)
    )
)
product_ru_button.click()
logo = '//img[@src="http://yanigen.com.ua/images/logo-2015.png"]'
WebDriverWait(driver, 100).until_not(
    EC.presence_of_element_located(
        (By.XPATH, logo)
    )
)
driver.quit()