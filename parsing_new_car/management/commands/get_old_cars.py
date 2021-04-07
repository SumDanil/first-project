import time
import requests
from bs4 import BeautifulSoup
from django.core.management import BaseCommand
from scraping.models import OldCar


def gen_url(page):
    return f'https://auto.ria.com/api/search/auto?indexName=auto%2Corder_auto%2Cnewauto_search&abroad=' \
      f'2&custom=1&page={page}&countpage=20&with_feedback_form=1&withOrderAutoInformer=1&with_last_id=1'


class Command(BaseCommand):
    def handle(self, *args, **options):
        cars = OldCar.objects.all()
        for car in cars:
            print(car.race)
            car.race = int(str(car.race).split()[0])
            car.save()

        exit()
        rec = requests.get(gen_url(0))
        count_page = int(rec.json()['result']['search_result_common']['count']/20)
        print(count_page)
        for g in range(13, count_page):
            print(f'Парсинг страницы {g} из {count_page}...')
            time.sleep(4)
            try:
                rec = requests.get(gen_url(g))
            except:
                time.sleep(4)
                rec = requests.get(gen_url(g))
            try:
                id_cars = rec.json()['result']['search_result']['ids']
            except:
                time.sleep(4)
                id_cars = rec.json()['result']['search_result']['ids']
            for i in id_cars:
                # print(i)
                # userId = info['userId']
                # info_id = requests.get(f'https://auto.ria.com/demo/bu/finalPage/users/{g}]langId=4')
                try:
                    car = requests.get(f'https://auto.ria.com/uk/bu/blocks/json/2931/293108/{i}?langId=4&lang_id=4')\
                        .json()
                except:
                    print(f'https://auto.ria.com/uk/bu/blocks/json/2931/293108/{i}?langId=4&lang_id=4')
                    continue
                userid = car['userId']
                try:
                    user_json = requests.get(f'https://auto.ria.com/demo/bu/finalPage/users/{userid}?langId=4').json()
                except:
                    print(f'https://auto.ria.com/demo/bu/finalPage/users/{userid}?langId=4')
                    exit()
                try:
                    user_name = user_json['userData']['name']
                except:
                    user_name = 'Нет имени'
                try:
                    id_car = car['autoData']['autoId']
                except:
                    continue
                phone = user_json['phones']
                if len(phone) >= 1:
                    phone = phone[0]['phone']
                else:
                    phone = 'номер не указан'
                car_brand = car['title']
                price_grn = car['USD']
                price_dol = car['USD']
                # volume = car['fuelName']
                date_add = car['addDate']
                vin = car['VIN']
                race = car['autoData']['race'].split()[0]
                # cityId = car['plateNumberData']['text']
                engine_type = car['autoData']['fuelName']
                region = car['stateData']['regionName']
                city = car['stateData']['name']
                type_of_transport = car['autoData']['categoryNameEng']
                years = car['autoData']['year']
                description = car['autoData']['description']
                photo = car['photoData']['seoLinkB']
                car = OldCar(
                    user_name=user_name,
                    phone=phone,
                    car_brand=car_brand,
                    price_grn=price_grn,
                    price_dol=price_dol,
                    date_add=date_add,
                    vin=vin,
                    race=race,
                    engine_type=engine_type,
                    region=region,
                    city=city,
                    type_of_transport=type_of_transport,
                    years=years,
                    description=description,
                    id=id_car,
                    photo=photo
                )
                try:
                    car.save()
                except:
                    print('Ошибка сохранения')
                    continue
                # print(id_car)

