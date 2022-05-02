import os
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

choice_of_currency = "//strong[@class = 'iss']"

hrn = "//span [@cid = '144']"
grn = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, hrn)
    )
)
grn.click()

usd = "//span [@cid = '199']"
usd_ = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, usd)
    )
)
usd_.click()