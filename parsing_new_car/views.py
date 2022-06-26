from django.core.paginator import Paginator
from django.shortcuts import render
from scraping.models import OldCar, Car, EngineType, Region, City, TypeofTransport, Year


def title(request):
    cars = Car.objects.all()
    # получаю запрос, по какой области фильтровать
    region = request.GET.get('oblast', '')

# нахожу минимальный прайс машин
    list_min_price = []
    iter_cars = Car.objects.all()
    for i in iter_cars:
        list_min_price.append(i.price_dol)
    min_price = (min(list_min_price))
    # print(f'{min_price = }')

# нахожу минимальный прайс машин
    list_max_price = []
    iter_cars = Car.objects.all()
    for i in iter_cars:
        list_max_price.append(i.price_dol)
    max_price = (max(list_max_price))
    # print(f'{max_price = }')

# нахожу минимальный пробег машин
    list_min_race = []
    iter_cars = Car.objects.all()
    for i in iter_cars:
        list_min_race.append(i.race)
    min_race = (min(list_min_race))
    # print(f'{min_race = }')

    # нахожу максимальный пробег машин
    list_max_race = []
    iter_cars = Car.objects.all()
    for i in iter_cars:
        list_max_race.append(i.race)
    max_race = (max(list_max_race))
    # print(f'{max_race = }')

# нахожу максимальный возраст
    list_max_years = []
    iter_cars = Year.objects.all()
    for i in iter_cars:
        list_max_years.append(i.years)
    max_years = (max(list_max_years))
    # print(f'{max_years = }')

# нахожу минимальный возраст
    list_min_years = []
    iter_cars = Year.objects.all()
    for i in iter_cars:
        list_min_years.append(i.years)
    min_years = (min(list_min_years))
    # print(f'{min_years = }')

# вывожу области из базы
    list_region = []
    iter_cars = Region.objects.all()
    for i in iter_cars:
        list_region.append(i.region)
    region_mas = set(list_region)
    # print(list_region)

    # print(f"{time.monotonic() - t}")
    # print(f"{OldCar.objects.count()}")

# фильтрую регион машины
    if len(region) > 5:
        cars = cars.filter(region__region=region)
        # print(cars.count())

# получаю запрос со странички с ценами
    price_ot = request.GET.get('price_ot', 0)
    price_do = request.GET.get('price_do', 0)
# фильтрую цену
    if price_ot:
        # print(f"{price_ot = }")
        cars = cars.filter(price_dol__gte=float(price_ot))
        min_price = request.GET.get('price_ot')
        # print(cars.count())

# фильтрую цену
    if price_do:
        # print(f"{price_do = }")
        cars = cars.filter(price_dol__lte=float(price_do))
        max_price = request.GET.get('price_do')
        # print(cars.count())

# получаю запрос с пробегами
    race_ot = request.GET.get('race_ot', 0)
    race_do = request.GET.get('race_do', 0)
# фильтрую пробег
    if race_ot:
        cars = cars.filter(race__gte=race_ot)
        min_race = request.GET.get('race_ot')
        # print(cars.count())
    if race_do:
        cars = cars.filter(race__lte=race_do)
        max_race = request.GET.get('race_do')
        # print(cars.count())

    age_ot = request.GET.get('age_ot', 0)
    age_do = request.GET.get('age_do', 0)

# фильтрую возраст машины
    if age_ot:
        cars = cars.filter(years__years__gte=age_ot)
        min_years = request.GET.get('age_ot')
        # print(cars.count())
        # print(age_ot)
    if age_do:
        cars = cars.filter(years__years__lte=age_do)
        max_years = request.GET.get('age_do')
        # print(cars.count())
        # print(age_do)
        print('1')
        print('2')
        print('changes only on master22')
        print('changes  on branch test3')
        print('test with vs code133')
        print('vs code change in git22')

    paginator = Paginator(cars.all(), 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    for new in page_obj:
        new.gggg()
    for city1 in page_obj:
        city1.aaaa()
    context = {
        'page_obj': page_obj,
        'min_race': min_race,
        'min_price': int(min_price),
        'max_price': int(max_price),
        'max_race': max_race,
        'max_years': max_years,
        'min_years': min_years,
        'region_mas': region_mas,
    }

    return render(request, 'parsing_new_car/HTML/title.html', context=context)
