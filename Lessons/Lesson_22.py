# #Selenium IDE WebDriver
# import os
# #
# from selenium import webdriver
#
# # import os
# # driver = webdriver.Firefox(os.getcwd())
# # driver.get(https://github.com/builuk1/builuk1-QA03/blob/master/Lesson19.py)
import os
import time

from selenium import webdriver

driver_path_chrome = os.getcwd() + '/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path_chrome)
driver.get('https://chromedriver.chromium.org/downloads')
time.sleep(5)
driver.quit()

# # for mac
# # EXE_PATH = r'path\to\chromedriver.exe' # EXE_PATH это путь до ранее загруженного нами файла chromedriver.exe
# # driver = webdriver.Chrome(executable_path=EXE_PATH)
# # driver.get('https://google.com')import os
#



driver_path_firefox = os.getcwd() + '/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path_firefox)
driver.get('https://chromedriver.chromium.org/downloads')
time.sleep(5)
driver.quit()

# #driver.close()
#
#
# driver.maximize_window()

# from selenium import webdriver
# import time
# dr = webdriver.Firefox(executable_path = '/geckodriver')
# dr.get('http://baidu.com')
# time.sleep(5)
# print('Browser will close')
# dr.quit()




#
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# # for mac
# # EXE_PATH = r'path\to\chromedriver.exe' # EXE_PATH это путь до ранее загруженного нами файла chromedriver.exe
# # driver = webdriver.Chrome(executable_path=EXE_PATH)
# # driver.get('https://google.com')import os
#
# # driver_path_chrome = os.getcwd() + 'chromedriver.exe'
# driver_path_firefox = s.getcwd() + '/Users/apple/PycharmProjects/pythonProjectQ03//geckodriver'
# s = Service(driver_path_firefox)
# d = Service('/Users/apple/PycharmProjects/pythonProjectQ03/geckodriver')
# driver = webdriver.Chrome(service=d)
# # driver.get('https://chromedriver.chromium.org/downloads')driver = webdriver.Firefox(service=s)
# driver.get('https://chromedriver.chromium.org/downloads')