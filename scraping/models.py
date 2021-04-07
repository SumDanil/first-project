from django.db import models


class Car(models.Model):
    name_base1 = 'Машина'
    # dvs = 'ДВС'
    # hybrid = 'Гибрид'
    # electro = 'Электро'
    # ENGINE_TYPE = [(dvs, 'ДВС'), (hybrid, 'Гибрид'), (electro, 'Электро')]
    # engine_type = models.CharField(max_length=50, choices=ENGINE_TYPE, default=dvs )
    name = models.CharField(max_length=50, blank=True, verbose_name='Имя пользователя')
    surname = models.CharField(max_length=50, blank=True, verbose_name='фамилия пользователя')
    price_grn = models.CharField(max_length=50, verbose_name='Цена в грн.')
    c = models.CharField(max_length=50, verbose_name='Цена в дол.')
    volume = models.CharField(max_length=50, verbose_name='Объём двигателя')
    car_brand = models.CharField(max_length=50, verbose_name='марка машины')
    date_add = models.CharField(max_length=50, verbose_name='дата добавления')
    phone = models.CharField(max_length=50, blank=True, verbose_name='номер телефона')
    vin = models.CharField(max_length=50, verbose_name='VIN код')
    race = models.CharField(max_length=50, verbose_name='пробег машины')
    cityId = models.CharField(max_length=50, blank=True, verbose_name='гос. номер')
    photo = models.ImageField(max_length=50, blank=True, verbose_name='фото')
    description = models.TextField(max_length=50, blank=True, verbose_name='описание')
    body_type = models.ForeignKey('BodyType', blank=True, on_delete=models.CASCADE, verbose_name='Тип кузова')
    fuel_type = models.ForeignKey('FuelType', blank=True, on_delete=models.CASCADE, verbose_name='Тип топлива')
    engine_type = models.ForeignKey('EngineType', on_delete=models.CASCADE, verbose_name='Тип двигателя')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, verbose_name='Область')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    type_of_transport = models.ForeignKey('TypeofTransport', on_delete=models.CASCADE, verbose_name='Тип транспорта')
    years = models.ForeignKey('Year', on_delete=models.CASCADE, verbose_name='Год')

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return self.name_base1


class BodyType(models.Model):
    CHOICES1 = (
        ('СД', 'Седан'),
        ('ХБ3', 'Хэтчбек 3 двери'),
        ('ХБ5', 'Хэтчбек 5 дверей'),
        ('УН', 'Универсал'),
        ('КБ', 'Кабриолет'),
        ('КП', 'Купэ'),
        ('Р', 'Родстер'),
        ('МН', 'Минивен'),
        ('МК', 'Микроавтобус'),
        ('ФР', 'Фургон'),
        ('ВН3', 'Внедорожник 3 двери'),
        ('ВН5', 'Внедорожник 5 дверей'),
    )
    body_type = models.CharField(max_length=50, verbose_name='Тип кузова', choices=CHOICES1,
                                 default='Выбери тип кузова')

    # sedan = models.CharField(max_length=50, verbose_name='Седан')
    # hatchbek3 = models.CharField(max_length=50, verbose_name='Хэтчбек3')
    # hatchbek5 = models.CharField(max_length=50, verbose_name='Хэтчбек5')
    # universal = models.CharField(max_length=50, verbose_name='Универсал')
    # cabriolet = models.CharField(max_length=50, verbose_name='Кабриолет')
    # compartment = models.CharField(max_length=50, verbose_name='Купэ')
    # rodster = models.CharField(max_length=50, verbose_name='Родстер')
    # minivan = models.CharField(max_length=50, verbose_name='Минивен')
    # minibus = models.CharField(max_length=50, verbose_name='микроавтобус')
    # van = models.CharField(max_length=50, verbose_name='Фургон')
    # suv3 = models.CharField(max_length=50, verbose_name='Внедорожник 3 двери')
    # suv5 = models.CharField(max_length=50, verbose_name='Внедорожник 5 дверей')
    # pickup = models.CharField(max_length=50, verbose_name='Пикап')

    class Meta:
        verbose_name = 'Тип кузова'
        verbose_name_plural = 'Типы кузовов'

    def __str__(self):
        return self.body_type


class FuelType(models.Model):
    CHOICES2 = (
        ('Газ', 'Газ'),
        ('Бензин', 'Бензин'),
        ('Газ/бензин', 'Газ/бензин'),
        ('Гибрид', 'Гибрид'),
        ('Электрика', 'Электрика'),
        ('Дизель', 'Дизель'),
    )
    fuel_type = models.CharField(max_length=50, verbose_name='Тип топлива', choices=CHOICES2,
                                 default='Выбери тип топлива')

    # gas = models.CharField(max_length=50, verbose_name='Газ')
    # petrol = models.CharField(max_length=50, verbose_name='Бензин')
    # gas_petrol = models.CharField(max_length=50, verbose_name='Газ/бензин')
    # hybrid = models.CharField(max_length=50, verbose_name='Гибрид')
    # electrician = models.CharField(max_length=50, verbose_name='Электрика')
    # diesel = models.CharField(max_length=50, verbose_name='Дизель')

    class Meta:
        verbose_name = 'Тип топлива'
        verbose_name_plural = 'Тип топлива'

    def __str__(self):
        return self.fuel_type


class EngineType(models.Model):
    CHOICES3 = (
        ('ДВС', 'ДВС'),
        ('Гибрид', 'Гибрид'),
        ('Эл. двигатель', 'Эл. двигатель'),
    )
    engine_type = models.CharField(max_length=50, verbose_name='Тип двигателя', choices=CHOICES3,
                                   default='Выбери тип двигателя')

    # dvs = models.CharField(max_length=50, verbose_name='ДВС')
    # hybrid = models.CharField(max_length=50, verbose_name='Гибрид')
    # hybrid = models.CharField(max_length=50, verbose_name='Эл. двигатель')

    class Meta:
        verbose_name = 'Тип двигателя'
        verbose_name_plural = 'Тип двигателей'


class Region(models.Model):
    region = models.CharField(max_length=50, verbose_name='Область')

    class Meta:
        verbose_name = 'Область'
        verbose_name_plural = 'Области'

    def __str__(self):
        return self.region


class City(models.Model):
    city = models.CharField(max_length=50, verbose_name='Город')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.city


class TypeofTransport(models.Model):
    CHOICES4 = (
        ('Пасажириская', 'Пасажириская'),
        ('Грузовой', 'Грузовой'),
        ('Грузо-пасажир', 'Грузо-пасажир'),
    )

    type_of_transport = models.CharField(max_length=50, verbose_name='Тип транспорта', choices=CHOICES4,
                                 default='Выбери тип топлива')
    
    class Meta:
        verbose_name = 'Тип транспорта'
        verbose_name_plural = 'Тип транспорта'

    def __str__(self):
        return self.type_of_transport


class Year(models.Model):
    years = models.CharField(max_length=50, verbose_name='Год')

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

    def gggg(self):
        if len(self.description) > 150:
            self.description = self.description[:150] + '...'

    def aaaa(self):
        if self.city == 'Дніпро (Дніпропетровськ)':
            self.city = 'Дніпро'



    class Meta:
        verbose_name = 'Б/У'
        verbose_name_plural = 'Б/У'

    def __str__(self):
        return self.car_brand

