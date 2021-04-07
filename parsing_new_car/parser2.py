import requests
import csv
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&country.import.usa.not=-1&price.' \
      'currency=1&abroad.not=0&custom.not=1&page=1&size=20'
# HEADERS Это словарь в котором будут заколовки. Для чего он нужен - для того что- бы сервер не посчитал меня за бота
# и не забинил. Таким образом имитируется работа браузера. (Смотреть в разделе 'сеть', констоли браузера)
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/89.0.4389.90 Safari/537.36'}
# HOST эта константа нужна ниже для ссылок
HOST = 'https://auto.ria.com'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('se', class_='proposition')



# функция на выполнение
def parse():
    html = get_html(URL)
    if html.status_code == 200:
       get_content(html.text)
    else:
        print('Error')