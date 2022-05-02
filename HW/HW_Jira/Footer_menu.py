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


footer_home_button = "//ul [@class = 'menu']/li/a[@href = '/en/']"
footer_home_ = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_home_button)
    )
)
footer_home_.click()


footer_prod_otrder = "//ul [@class = 'menu']/li/a[@href = '/en/productstoorder']"
footer_prod_otrd = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_prod_otrder)
    )
)
footer_prod_otrd.click()


logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()



footer_catalog = "//div[@class = 'content']/ul [@class = 'menu']//li/a[@href = '/en/categories']"
footer_catal = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_catalog)
    )
)
footer_catal.click()



logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()



footer_to_clients = "//ul [@class = 'menu']//li/a[@href = '/en/toclients']"
footer_to_client = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_to_clients)
    )
)
footer_to_client.click()



logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()



footer_about_us = "//li/a [contains(text(),'About us')]"
footer_about_ = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_about_us)
    )
)
footer_about_.click()



logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()



footer_contacts_button = "//ul[@class ='menu']/li/a[@href='/en/contacts']"
footer_contacts_but = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH,footer_contacts_button)
    )
)
footer_contacts_but.click()



logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()
