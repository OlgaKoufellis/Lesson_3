import os
import time

from selenium import webdriver

driver_path_chrome = os.getcwd() + '/drivers/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path_chrome)
driver.get('https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html')


# q1_full_xpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[2]/td[3]/input'
q1_full_xpath = '//input[@name = "q1"]'
q1 = driver.find_element('xpath',q1_full_xpath)
q1.send_keys('some')

q9_a_full_xpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/input'
q9_a = driver.find_element('xpath',q9_a_full_xpath)
q9_a.click()

q10_a_full_xpath = '//input[@name = "q10" and @value = "a"]'
q10_a = driver.find_element('xpath',q10_a_full_xpath)
q10_a.click()

# q19_a_full_xpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[3]/tbody/tr[2]/td[2]/input'
q19_a_full_xpath = '//input[@name = "q19" and @value = "a"]'
q19_a = driver.find_element('xpath',q19_a_full_xpath)
q19_a.click()

q20_a_full_xpath = '//input[@name = "q20" and @value = "a"]'
q20_a = driver.find_element('xpath',q20_a_full_xpath)
q20_a.click()

q21_a_full_xpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[3]/tbody/tr[6]/td[2]/input'
q21_a = driver.find_element('xpath',q21_a_full_xpath)
q21_a.click()

time.sleep(5)
driver.quit()


# driver_path_firefox = os.getcwd() + '/drivers/geckodriver'
# driver = webdriver.Firefox(executable_path=driver_path_firefox)
# driver.get('https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html')
# time.sleep(5)
# driver.quit()