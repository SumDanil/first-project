from django.db import models


class Car(models.Model):
    user_name = models.CharField(max_length=50, blank=True, verbose_name='Имя пользователя')
    price_grn = models.CharField(max_length=50, blank=True, verbose_name='Цена в грн.')
    price_dol = models.CharField(max_length=50, blank=True, verbose_name='Цена в дол.')
    car_brand = models.CharField(max_length=50, blank=True, verbose_name='марка машины')
    date_add = models.CharField(max_length=50, blank=True, verbose_name='дата добавления')
    phone = models.CharField(max_length=50, blank=True, verbose_name='номер телефона')
    vin = models.CharField(max_length=50, blank=True, verbose_name='VIN код')
    race = models.CharField(max_length=50, blank=True, verbose_name='пробег машины')
    photo = models.TextField(blank=True, verbose_name='Cсылка на фото')
    description = models.TextField(max_length=50, blank=True, verbose_name='описание')
    engine_type = models.ForeignKey('EngineType', on_delete=models.CASCADE, verbose_name='Тип двигателя')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, verbose_name='Область')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    type_of_transport = models.ForeignKey('TypeofTransport', on_delete=models.CASCADE, verbose_name='Тип транспорта')
    years = models.ForeignKey('Year', on_delete=models.CASCADE, verbose_name='Год')

    def gggg(self):
        if len(self.description) > 150:
            self.description = self.description[:150] + '...'

    def aaaa(self):
        if self.city == 'Дніпро (Дніпропетровськ)':
            self.city = 'Дніпро'

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


class EngineType(models.Model):
    engine_type = models.CharField(max_length=50, blank=True, unique=True, verbose_name='Тип двигателя')

    class Meta:
        verbose_name = 'Тип двигателя'
        verbose_name_plural = 'Тип двигателей'

    def __str__(self):
        return self.engine_type


class Region(models.Model):
    region = models.CharField(max_length=50, blank=True, unique=True, verbose_name='Область')

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Области'

    def __str__(self):
        return self.region


class City(models.Model):
    city = models.CharField(max_length=50, blank=True, unique=True, verbose_name='Город')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.city


class TypeofTransport(models.Model):
    type_of_transport = models.CharField(max_length=50, blank=True, unique=True, verbose_name='Тип транспорта')
    
    class Meta:
        verbose_name = 'Тип транспорта'
        verbose_name_plural = 'Тип транспорта'

    def __str__(self):
        return self.type_of_transport


class Year(models.Model):
    years = models.IntegerField(blank=True, unique=True, verbose_name='Год')

    class Meta:
        verbose_name = 'Год'
        verbose_name_plural = 'Года'

    def __str__(self):
        return self.years


class NewCar(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование')
    link = models.TextField(max_length=50, verbose_name='Ссылка')
    usd_prise = models.DecimalField(max_digits=15, decimal_places=4, verbose_name='Цена в дол.')
    city = models.CharField(max_length=50, verbose_name='Город')
    uah_prise = models.DecimalField(max_digits=15, decimal_places=4, verbose_name='Цена в грн')

    class Meta:
        verbose_name = 'Новая машина'
        verbose_name_plural = 'Новые машины'

    def __str__(self):
        return self.title


class OldCar(models.Model):
    user_name = models.CharField(max_length=250, blank=True, verbose_name='Имя продавца')
    phone = models.CharField(max_length=250, blank=True, verbose_name='Номер телефона')
    car_brand = models.CharField(max_length=250, blank=True, verbose_name='Машина')
    price_grn = models.DecimalField(max_digits=15, decimal_places=4, blank=True, verbose_name='Цена в грн.')
    price_dol = models.DecimalField(max_digits=15, decimal_places=4, blank=True, verbose_name='Цена в дол.')
    date_add = models.CharField(max_length=250, blank=True, verbose_name='Дата добавления')
    vin = models.CharField(max_length=250, blank=True, verbose_name='VIN код')
    race = models.IntegerField(blank=True, verbose_name='Пробег')
    engine_type = models.CharField(max_length=250, blank=True, verbose_name='Тип дввигателя')
    region = models.CharField(max_length=250, blank=True, verbose_name='Область')
    city = models.CharField(max_length=250, blank=True, verbose_name='Город')
    type_of_transport = models.CharField(max_length=250, blank=True, verbose_name='Тип двигателя')
    years = models.IntegerField(blank=True, verbose_name='Год')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.TextField(blank=True, verbose_name='Cсылка на фото')

    class Meta:
        verbose_name = 'Б/У'
        verbose_name_plural = 'Б/У'

    def __str__(self):
        return self.car_brand

