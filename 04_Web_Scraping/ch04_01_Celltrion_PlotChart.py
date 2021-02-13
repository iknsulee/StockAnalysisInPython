import pandas as pd
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
html = BeautifulSoup(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text, "lxml")
pgrr = html.find('td', class_='pgRR')
s = str(pgrr.a['href']).split('=')
last_page = s[-1]
print(last_page)

df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'
for page in range(300, int(last_page)+1):
    page_url = '{}&page={}'.format(sise_url, page)  
    # df = df.append(pd.read_html(page_url, header=0)[0])
    df = df.append(pd.read_html(requests.get(page_url, headers={'User-agent': 'Mozilla/5.0'}).text)[0])
    
df = df.dropna()
df = df.iloc[0:30] 
df = df.sort_values(by='날짜') 

plt.title('Celltrion (close)')
plt.xticks(rotation=45) 
plt.plot(df['날짜'], df['종가'], 'co-')
plt.grid(color='gray', linestyle='--')
plt.show()
