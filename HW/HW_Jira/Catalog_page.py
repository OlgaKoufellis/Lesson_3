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

catalog_but = "//ul [@class = 'menumain']/li/a[@href = '/en/categories']"
catalog_butt = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, catalog_but)
    )
)
catalog_butt.click()

wallets_purses = "//h3 [@class= 'catProductTitle']/a [@href = '/en/shop/wallets-purses']"
wallets_purses_picture = "//div [@class= 'spacer gkImage']/a/img [@alt = 'neat2_20']"

documents_holders = "//h3 [@class= 'catProductTitle']/a [@href = '/en/shop/documentsholders']"
documents_holders_picture = "//div [@class= 'spacer gkImage']/a/img [@alt = 'compact_20']"

cardholders_key_holders = "//h3 [@class= 'catProductTitle']/a [@href = '/en/shop/cardholders']"
cardholders_key_holders_picture = "//div [@class= 'spacer gkImage']/a/img [@alt = 'simple2_20']"

different = "//h3 [@class= 'catProductTitle']/a [@href = '/en/shop/different']"
different_picture = "//div [@class= 'spacer gkImage']/a/img [@alt = 'strip_04']"

woodbooksa5 = "//h3 [@class= 'catProductTitle']/a [@href = '/en/shop/woodbooksa5']"
woodbooksa5_picture = "//div [@class= 'spacer gkImage']/a/img[@alt='dsc_0607-2']"

woodbooksa6 = "//h3 [@class= 'catProductTitle']/a [@href = '/en/shop/woodbooksa6']"
woodbooksa6_picture = "//div [@class= 'spacer gkImage']/a/img[@alt='categ7']"



