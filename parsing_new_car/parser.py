import requests
import csv
from bs4 import BeautifulSoup

URL = 'https://auto.ria.com/uk/newauto/search/?page=1&show_in_search=1&markaId=67&size=10'
# HEADERS Это словарь в котором будут заколовки. Для чего он нужен - для того что- бы сервер не посчитал меня за бота
# и не забинил. Таким образом имитируется работа браузера. (Смотреть в разделе 'сеть', констоли браузера)
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/89.0.4389.90 Safari/537.36'}
# HOST эта константа нужна ниже для ссылок
HOST = 'https://auto.ria.com'
FILE = 'cars.csv'


#items - объекты которые нужно сохранять
#path - путь куда необходимо сохранять
def sav_file(items, path):
    #открываем файлпо заданому пути, а если его не будет, то он будет создан. newline='' - что б небыло пустых строк
    with open(path, 'w', newline='') as file:
        #delimiter=';' для того что бы файл нормально открывался в excel
        #file - указывает на открытый файл
        writer = csv.writer(file, delimiter=';')
        # ниже записываю строки в csv файл
        # ни ниже передвётся в виде списка колонки для записи
        writer.writerow(['Марка ', 'Ссылка', 'Цена в доларах', 'Город', 'Цена в гривнах'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['usd_prise'], item['city'], item['uah_prise']])





# url - url страницы с которой нужно получить контент
#  params - нужен для передачи дополнительныхпараметров первому аргументу.
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='page-item mhide')
    if pagination:
        # определение конечной страничке в списке
        return int(pagination[-1].get_text())
    else:
        return 1


#парсинг html сайта
#парсинг html сайта
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='proposition')
    # print(items)

    cars = []
    for item in items:
        # проверка на наличие цены в гривнах
        uah_prise = item.find('span', class_='size16')
        if uah_prise:
            uah_prise = uah_prise.get_text(strip=True)
        else:
            print('Цену уточняйте')
        cars.append({
            'title': item.find('span', class_='link').get_text(strip=True),
            'link': HOST + item.find('a', class_='proposition_link').get('href'),
            'usd_prise': item.find('span', class_='green').get_text(strip=True),
            'city': item.find('span', class_='item region').get_text(strip=True),
            'uah_prise': uah_prise('span', class_='green').get_text(strip=True),
        })
    return cars


# функция на выполнение
def parse():
    html = get_html(URL)
    if html.status_code == 200:
        cars = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count+1):
            print(f'Парсинг страницы {page} из {pages_count}...')
            html = get_html(URL, params={'page': page})
            cars.extend(get_content(html.text))
        # cars = get_content(html.text)
        sav_file(cars, FILE)
        print(cars)
    else:
        print('Error')



parse()
