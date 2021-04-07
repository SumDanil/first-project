from django.core.paginator import Paginator
from django.shortcuts import render
from scraping.models import OldCar


def title(request):
    cars = OldCar.objects
    print(request.GET)
    region = request.GET.get('oblast', '')

    list_min_price = []
    iter_cars = OldCar.objects.all()
    for i in iter_cars:
        list_min_price.append(i.price_dol)
    min_price = (min(list_min_price))
    print(min_price)

    list_max_price = []
    iter_cars = OldCar.objects.all()
    for i in iter_cars:
        list_max_price.append(i.price_dol)
    max_price = (max(list_max_price))
    print(max_price)

    list_min_race = []
    iter_cars = OldCar.objects.all()
    for i in iter_cars:
        list_min_race.append(i.race)
    min_race = (min(list_min_race))
    print(min_race)

    list_max_race = []
    iter_cars = OldCar.objects.all()
    for i in iter_cars:
        list_max_race.append(i.race)
    max_race = (max(list_max_race))
    print(max_race)

    list_max_years = []
    iter_cars = OldCar.objects.all()
    for i in iter_cars:
        list_max_years.append(i.years)
    max_years = (max(list_max_years))
    print(max_years)

    list_min_years = []
    iter_cars = OldCar.objects.all()
    for i in iter_cars:
        list_min_years.append(i.years)
    min_years = (min(list_min_years))
    print(min_years)


    import time
    t = time.monotonic()

    list_region = []
    iter_cars = OldCar.objects.all()
    for i in iter_cars:
        list_region.append(i.region)
    region_mas = set(list_region)

    print(f"{time.monotonic() - t}")
    print(f"{OldCar.objects.count()}")

    if len(region) > 5:
        cars = cars.filter(region=region)

    price_ot = request.GET.get('price_ot', 0)
    price_do = request.GET.get('price_do', 0)
    if price_ot:
        # print(f"{price_ot = }")
        cars = cars.filter(price_dol__gte=float(price_ot))

    if price_do:
        # print(f"{price_do = }")
        cars = cars.filter(price_dol__lte=float(price_do))

    race_ot = request.GET.get('race_ot', 0)
    race_do = request.GET.get('race_do', 0)
    if race_ot:
        cars = cars.filter(race__gte=race_ot)
    if race_do:
        cars = cars.filter(race__lte=race_do)

    age_ot = request.GET.get('age_ot', 0)
    age_do = request.GET.get('age_do', 0)
    if age_ot:
        cars = cars.filter(years__gte=age_ot)
    if age_do:
        cars = cars.filter(years__lte=age_do)



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


