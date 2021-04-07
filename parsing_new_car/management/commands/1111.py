from scraping.models import OldCar


list_min_price = []
iter_cars = OldCar.objects.all()
for i in iter_cars:
    list_min_price.append(i.price_dol)
print(min(list_min_price))

import time

t = time.monotonic()

list_region = []
iter_cars = OldCar.objects.all()
for i in iter_cars:
    if i.region not in list_region:
        list_region.append(i.region)
region_mas = list_region

print(f"{time.monotonic() - t}")
print(f"{OldCar.objects.count()}")