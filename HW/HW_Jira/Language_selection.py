import os
# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path_chrome = os.getcwd() + '/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path_chrome)

# Open site
driver.get('https://www.yanigen.com.ua')
driver.maximize_window()
wait = WebDriverWait(driver, 20)

Lenguage_selection = "//div[@class = 'pretext']"

ua = "//ul[@class = 'lang-inline']/li/a[@href = '/ua/']"
ua_ = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, ua)
    )
)
ua_.click()

ru = "//ul[@class = 'lang-inline']/li/a[@href = '/ru/']"
ru_ = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, ru)
    )
)
ru_.click()

en = "//ul[@class = 'lang-inline']/li/a[@href = '/en/']"
en_ = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, en)
    )
)
en_.click()