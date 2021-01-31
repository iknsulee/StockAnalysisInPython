import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas
import datetime

url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'

# request_result = requests.get(url)
# print(request_result)
# print(request_result.content)

dayPriceHtml = urlopen(url)
print(dayPriceHtml)
dayPriceSource = BeautifulSoup(dayPriceHtml.read(), "html.parser")
