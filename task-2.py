# б) Получить все цены с динамического сайта маркетплейса, используя
# selenium.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome = webdriver.Chrome()

url = 'https://alser.kz/'

chrome.get(url)

time.sleep(5)

prices = chrome.find_elements(by=By.CLASS_NAME, value='card__price') # ищем по названию класса

for price in prices:
    print(price.text)