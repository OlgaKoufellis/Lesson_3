import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


driver_path_chrome = os.getcwd() + '/drivers/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path_chrome)
driver.get('https://www.yanigen.com.ua')
time.sleep(5)
driver.maximize_window()
# driver_screenshot_as_file(yanigen.png)
#
home_ru = "//a [contains(text(),'ГЛАВНАЯ']"
home2_ru = "//ul[@class='menumain']/li/a[@href='/ru/']"
home_ua = "//a [contains(text(),'ГОЛОВНА']"
home_eng = "//a [contains(text(),'MAIN']"
#
button = "//ul[@class = 'menumaim']/li/a[@href = '/en/productstoorder']"
about_us_button = "//a [contains (text (), 'ABOUT US')]"

catalog_button = "//li/a [contains(text (), 'CATALOG')]"
contacts_button = "//ul[@class ='menumain']/li/a[@href='/en/contacts']"
footer_contacts_button = "//ul[@class ='menu']/li/a[@href='/en/contacts']"
footer_about_us = "//li/a [contains(text(),'About us')]"

# sub_bu = "//td[@class='acysubbuttons']/input[@type='submit']"
# sub_but = WebDriverWait(driver, 60).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, sub_bu)
#     )
# )
# sub_but.click()



body_button_go_to_catalog = "//ul[@class = 'menu']/li/a[@href = '/en/categories']"
body_button_go_to_ = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH,body_button_go_to_catalog)
    )
)
body_button_go_to_.click()
#
driver_path_chrome = os.getcwd() + '/drivers/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path_chrome)
driver.get('https://bank.gov.ua/ua/markets/exchangerates')
with webdriver.Chrome(executable_path=driver_path_chrome) as driver:
    # Open URL
    driver.get('http://yanigen.com.ua/ru/')
    driver.maximize_window()
    # Setup wait for later
    wait = WebDriverWait(driver, 20)

    # Store the ID of the original window
    original_window = driver.current_window_handle

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    # Click the link which opens in a new window
    # driver.find_element(By.XPATH, "//ul[@class='menumain']/li/a[@href='/ru/']").click()
    driver.switch_to.new_window('tab')
    driver.get("https://seleniumhq.github.io")
    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Wait for the new tab to finish loading content
    wait.until(EC.title_is("Selenium"))