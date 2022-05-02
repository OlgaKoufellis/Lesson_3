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
wait = WebDriverWait(driver, 220)

catalog_but = "//ul [@class = 'menumain']/li/a[@href = '/en/categories']"
catalog_butt = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, catalog_but)
    )
)
catalog_butt.click()


#####
wallets_purses = "//h3 [@class= 'catProductTitle']/a [@href = '/en/shop/wallets-purses']"
wallets_purse = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, wallets_purses)
    )
)
wallets_purse.click()

logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()


catalog_but = "//ul [@class = 'menumain']/li/a[@href = '/en/categories']"
catalog_butt = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, catalog_but)
    )
)
catalog_butt.click()

###
wallets_purses_picture = "//div [@class= 'spacer gkImage']/a/img [@alt = 'neat2_20']"
wallets_purse_pictures = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, wallets_purses_picture)
    )
)
wallets_purse_pictures.click()

logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()
catalog_but = "//ul [@class = 'menumain']/li/a[@href = '/en/categories']"
catalog_butt = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, catalog_but)
    )
)
catalog_butt.click()

####
documents_holders = "//h3 [@class= 'catProductTitle']/a [@href = '/en/shop/documentsholders']"
documents_holder = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, documents_holders)
    )
)
documents_holder.click()

logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()
catalog_but = "//ul [@class = 'menumain']/li/a[@href = '/en/categories']"
catalog_butt = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, catalog_but)
    )
)
catalog_butt.click()

####
documents_holders_picture = "//div [@class= 'spacer gkImage']/a/img [@alt = 'compact_20']"
documents_holder_pictures = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, documents_holders_picture)
    )
)
documents_holder_pictures.click()

logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()
catalog_but = "//ul [@class = 'menumain']/li/a[@href = '/en/categories']"
catalog_butt = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, catalog_but)
    )
)
catalog_butt.click()

# ####
cardholders_key_holders = "//h3 [@class= 'catProductTitle']/a [@href = '/en/shop/cardholders']"
cardholders_key_holder = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, cardholders_key_holders)
    )
)
cardholders_key_holder.click()

logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()
catalog_but = "//ul [@class = 'menumain']/li/a[@href = '/en/categories']"
catalog_butt = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, catalog_but)
    )
)
catalog_butt.click()

####
cardholders_key_holders_picture = "//div [@class= 'spacer gkImage']/a/img [@alt = 'simple2_20']"
cardholders_key_holder_pic = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, cardholders_key_holders_picture)
    )
)
cardholders_key_holder_pic.click()

logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()
catalog_but = "//ul [@class = 'menumain']/li/a[@href = '/en/categories']"
catalog_butt = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, catalog_but)
    )
)
catalog_butt.click()

####
different = "//h3 [@class= 'catProductTitle']/a [@href = '/en/shop/different']"
differents = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, different)
    )
)
differents.click()

logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()
catalog_but = "//ul [@class = 'menumain']/li/a[@href = '/en/categories']"
catalog_butt = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, catalog_but)
    )
)
catalog_butt.click()

####
different_picture = "//div [@class= 'spacer gkImage']/a/img [@alt = 'strip_04']"
different_pic = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, different_picture)
    )
)
different_pic.click()

logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()
catalog_but = "//ul [@class = 'menumain']/li/a[@href = '/en/categories']"
catalog_butt = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, catalog_but)
    )
)
catalog_butt.click()

####
woodbooksa5 = "//h3 [@class= 'catProductTitle']/a [@href = '/en/shop/woodbooksa5']"
woodbooksa_5 = WebDriverWait(driver,120).until(
    EC.element_to_be_clickable(
        (By.XPATH, woodbooksa5)
    )
)
woodbooksa_5.click()

logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()
catalog_but = "//ul [@class = 'menumain']/li/a[@href = '/en/categories']"
catalog_butt = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, catalog_but)
    )
)
catalog_butt.click()

####
woodbooksa5_picture = "//div [@class= 'spacer gkImage']/a/img[@alt='dsc_0607-2']"
woodbooksa_5_pic = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, woodbooksa5_picture)
    )
)
woodbooksa_5_pic.click()

logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()
catalog_but = "//ul [@class = 'menumain']/li/a[@href = '/en/categories']"
catalog_butt = WebDriverWait(driver,120).until(
    EC.element_to_be_clickable(
        (By.XPATH, catalog_but)
    )
)
catalog_butt.click()

####
woodbooksa6 = "//h3 [@class= 'catProductTitle']/a [@href = '/en/shop/woodbooksa6']"
woodbooksa_6 = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, woodbooksa6)
    )
)
woodbooksa_6.click()

logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()
catalog_but = "//ul [@class = 'menumain']/li/a[@href = '/en/categories']"
catalog_butt = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, catalog_but)
    )
)
catalog_butt.click()

####
woodbooksa6_picture = "//div [@class= 'spacer gkImage']/a/img[@alt='categ7']"
woodbooksa6_pic = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, woodbooksa6_picture)
    )
)
woodbooksa6_pic.click()

logo = "//div [@class = 'toolbar-logo']/h2/a/img[@src = 'http://www.yanigen.com.ua/images/logo-2015.png']"
log = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, logo)
    )
)
log.click()
catalog_but = "//ul [@class = 'menumain']/li/a[@href = '/en/categories']"
catalog_butt = WebDriverWait(driver,220).until(
    EC.element_to_be_clickable(
        (By.XPATH, catalog_but)
    )
)
catalog_butt.click()



