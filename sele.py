from selenium import webdriver
import os
import time
from bs4 import BeautifulSoup
# Webdriver config for Heroku
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

''' Webdriver is needed because Thunderpokt uses JS to load the data and requests
    only gives you the first instance of HTML from the website without the data
    or output from JS.'''
driver.get("https://thunderpokt.fi/analytics")
# Program sleeps so that driver gets full website
time.sleep(8)
# Webscrap the driver
soup = BeautifulSoup(driver.page_source, 'html.parser')
# Get location of all tags needed
driver.quit()
data = soup.find('body', class_='h-full').find_all('h4', class_='text-xl font-semibold')
# Manually split and save in variables to avoid time consuming for loops
apy = data[0].text.split(" ")
apy_number = apy[0]+apy[1]
apy_name = apy[3]
dr = data[1].text.split(" ")
dr_number = dr[0]+dr[1]
dr_name = dr[3]
tts = data[2].text.split(" ")
tts_number = tts[0]
tts_name = tts[2]
_1d = data[4].text.split(" ")
_1d_number = _1d[0]
_1d_name = _1d[2]
_3d = data[5].text.split(" ")
_3d_number = _3d[0]
_3d_name = _3d[2]
_7d = data[6].text.split(" ")
_7d_number = _7d[0]
_7d_name = _7d[2]
# Printing just for sanity check lol
print(apy_name, apy_number)
print(dr_name, dr_number)
print(tts_name, tts_number)
print(_1d_name, _1d_number)
print(_3d_name, _3d_number)
print(_7d_name, _7d_number)
