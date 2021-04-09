import time
import requests
from bs4 import BeautifulSoup
from django.core.management import BaseCommand
from scraping.models import Car, EngineType, Region, City, TypeofTransport, Year


def gen_url(page):
    return f'https://auto.ria.com/api/search/auto?indexName=auto%2Corder_auto%2Cnewauto_search&abroad=' \
      f'2&custom=1&page={page}&countpage=20&with_feedback_form=1&withOrderAutoInformer=1&with_last_id=1'


class Command(BaseCommand):
    def handle(self, *args, **options):
        # cars = Car.objects.all()
        # for car in cars:
        #     print(car.race)
        #     car.race = int(str(car.race).split()[0])
        #     car.save()
        #
        # exit()
        rec = requests.get(gen_url(0))
        count_page = int(rec.json()['result']['search_result_common']['count']/20)
        print(count_page)
        for g in range(65, count_page):
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
                date_add = car['addDate']
                vin = car['VIN']
                try:
                    race = int(car['autoData']['race'].split()[0])
                except:
                    print('Без пробега')
                    race = 0
                engine_type = car['autoData']['fuelName']
                region = car['stateData']['regionName']
                city = car['stateData']['name']
                type_of_transport = car['autoData']['categoryNameEng']
                years = car['autoData']['year']
                description = car['autoData']['description']
                photo = car['photoData']['seoLinkB']

                car_enginetype = EngineType(
                    engine_type=engine_type,
                )
                try:
                    car_enginetype.save()
                except:
                    # print('Ошибка сохранения engine_type ')
                    car_enginetype = EngineType.objects.filter(engine_type=engine_type).first()

                car_region = Region(
                    region=region,
                )
                try:
                    car_region.save()
                except:
                    # print('Ошибка сохранения car_region')
                    car_region = Region.objects.filter(region=region).first()

                car_city = City(
                    city=city,
                )
                try:
                    car_city.save()
                except:
                    # print('Ошибка сохранения car_city')
                    car_city = City.objects.filter(city=city).first()

                car_typeofTransport = TypeofTransport(
                    type_of_transport=type_of_transport,
                )
                try:
                    car_typeofTransport.save()
                except:
                    # print('Ошибка сохранения car_typeofTransport')
                    car_typeofTransport = TypeofTransport.objects.filter(type_of_transport=type_of_transport).first()

                car_year = Year(
                    years=years,
                )
                try:
                    car_year.save()
                except:
                    # print('Ошибка сохранения car_year')
                    car_year = Year.objects.filter(years=years).first()

                car = Car(
                    user_name=user_name,
                    phone=phone,
                    car_brand=car_brand,
                    price_dol=price_dol,
                    date_add=date_add,
                    vin=vin,
                    race=race,
                    description=description,
                    id=id_car,
                    photo=photo,
                    engine_type=car_enginetype,
                    region=car_region,
                    city=car_city,
                    type_of_transport=car_typeofTransport,
                    years=car_year,
                )
                try:
                    car.save()
                except:
                    print('Ошибка сохранения car')
                    continue


