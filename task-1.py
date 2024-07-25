# а) Получить курс валют с динамического сайта погоды, используя selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome = webdriver.Chrome()

url = 'https://nationalbank.kz/ru/exchangerates/ezhednevnye-oficialnye-rynochnye-kursy-valyut'

chrome.get(url)

time.sleep(5)

currencies = chrome.find_elements(by=By.TAG_NAME, value='td') # ищем по названию тэга

for currency in currencies:
    print(currency.text.strip()) # убираем лишние пробелы