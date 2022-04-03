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
apy = data[0].text
dr = data[1].text
tts = data[2].text
_1d = data[4].text
_3d = data[5].text
_7d = data[6].text
print(apy, dr, tts, _1d, _3d, _7d)
