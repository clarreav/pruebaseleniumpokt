
import requests
from selenium import webdriver
import os
import time
from bs4 import BeautifulSoup
from urllib import response
from telegram.ext import *

API_KEY = "5128041686:AAH6KL80cI7rT9cIJH0BwjOITJpq4dyd6Rc"


def handle_message(update, context):
    text = update.message.text

    response = create_responses(text)
    update.message.reply_text(response)


def create_responses(input_text):
    if input_text == "/start":
        return "Welcome, you can get the stats of tpokt by typing in stats or get the contract addresses of tpokt and " \
               "wtpokt with the word contract "
    if input_text == "stats":
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
        # Quit the driver to get resources back
        driver.quit()
        # Get location of all tags needed
        data = soup.find('body', class_='h-full').find_all('h4', class_='text-xl font-semibold')
        # Manually split and save in variables to avoid time consuming for loops
        apy = data[0].text.split(" ")
        apy_number = apy[0] + apy[1]
        apy_name = apy[3]
        dr = data[1].text.split(" ")
        dr_number = dr[0] + dr[1]
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
        return apy_name+": "+apy_number+"\n"+dr_name+": "+dr_number+"\n"+tts_name+": "+tts_number+"\n"+_1d_name+": "+_1d_number+"\n"+_3d_name+": "+_3d_number+"\n"+_7d_name+": "+_7d_number
    if input_text == "contract":
        return "TPOKT: 0x5430a0B6C11f870571ffA891d59dec8C4608Ea9A & WTPOKT: 0x301595f6fd5f69faD7a488DaCB8971e7c0C2f559"
    else:
        return "Sorry, i didnt understand you - try stats to get the global tpokt stats and contract for the contracts"


def main():
    updater = Updater(API_KEY)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling(0)


if __name__ == "__main__":
    main()
