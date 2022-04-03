from selenium import webdriver
import os
import time
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
driver.get("https://thunderpokt.fi/analytics")
time.sleep(8)
soup = BeautifulSoup(driver.page_source, 'html.parser')
data = soup.find('body', class_='h-full').find_all('h4', class_='text-xl font-semibold')
apy = data[0].text.split(" ")
apy_number = apy[0]
apy_name = apy[2]
dr = data[1].text.split(" ")
dr_number = dr[0]
dr_name = dr[2]
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
print(apy_name, apy_number)
