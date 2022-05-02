import os
# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path_chrome = os.getcwd() + '/HW_Jira/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path_chrome)

# Open site
driver.get('https://www.yanigen.com.ua')
driver.maximize_window()
# wait = WebDriverWait(driver, 20)


#check main menu
logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
but_home_ru = "//a [contains(text(),'ГЛАВНАЯ']"
but_home_ua = "//a [contains(text(),'ГОЛОВНА']"
byt_home_eng = "//a [contains(text(),'MAIN']"

product_order_but = "//ul [@class = 'menumain']/li/a[@href = '/en/productstoorder']"

catalog_but = "//ul [@class = 'menumain']/li/a[@href = '/en/categories']"

to_clients_but = "//ul [@class = 'menumain']/li/a[@href = '/en/toclients']"

about_us = "//ul [@class = 'menumain']/li/a[@href = '/en/aboutus']"

contact_ua = "//ul [@class = 'menumain']/li/a[@href = '/en/contacts']"

########   slider
slider1_main_menu = "//div[@class = 'gkIsWrapper-gk_shop_and_buy ']" \
                   "/div/div/div/div/p/a [@href = 'http://yanigen.com.ua/en/shop/woodbooksa6']"
slider2_main_menu = "//div[@class = 'gkIsWrapper-gk_shop_and_buy ']" \
                    "/div/div/div/div/h3/a [@href = 'http://yanigen.com.ua/en/shop/woodbooksa6']"


picture_1 = "//a/img[@src = '/images/stories/virtuemart/product/compact_07.png']"
picture_2 = "//div/a/img[@src = '/images/stories/virtuemart/product/heirloom3_26.png']"
picture_3 = "//div/a/img[@src = '/images/stories/virtuemart/product/img_2743.png']"
picture_4 = "//div/a/img[@src = '/images/stories/virtuemart/product/zipper_15.png']"
picture_5 = "//div/a/img[@src = '/images/stories/virtuemart/product/neat2_20.png']"
piture_6 = "//div/a/img[@src = '/images/stories/virtuemart/product/heirloom2_25.png']"

body_button_go_to_catalog = "//ul[@class = 'menu']/li/a[@href = '/en/categories']"
body_button_go_to_ = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable(
        (By.XPATH,body_button_go_to_catalog)
    )
)
body_button_go_to_.click()

driver.switch_to.new_window('tab')
driver.get("https://www.yanigen.com.ua")
wait = WebDriverWait(driver, 20)
wait.until(EC.number_of_windows_to_be(2))

# sibscribe_to_news = "//div/h3 [contains(text(), 'SUBSCRIBE TO NEWS')]"
subscribe_but = "//td[@class='acysubbuttons']/input[@type='submit']"
subscribe_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, subscribe_but)
    )
)
subscribe_button.click()







