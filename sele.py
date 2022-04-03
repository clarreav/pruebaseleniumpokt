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
apy, apyn = data[0].text.split(" ")
dr, drn = data[1].text.split(" ")
tts, ttsn = data[2].text.split(" ")
_1d, _1dn = data[4].text.split(" ")
_3d, _3dn = data[5].text.split(" ")
_7d, _7dn = data[6].text.split(" ")
print(apyn, apy)
