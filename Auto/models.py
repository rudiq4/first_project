from django.db import models
from . import const  # для областей


class VehicleType(models.Model):
    veh_type = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        default=None
    )
    flag = models.BooleanField(default=True, verbose_name='Act/Deact')

    def __str__(self):
        return "%s" % self.veh_type

    class Meta:
        verbose_name = 'Тип т/з'
        verbose_name_plural = 'Типи т/з'


class Vehicle(models.Model):
    FUEL_CHOICES = (
        ('P', 'petrol'),
        ('D', 'diesel'),
        ('L', 'lpg'),
        ('H', 'hybrid'),
        ('E', 'electro')
    )
    LOCATION_CHOICES = (
        (0, "---"),
        (1, const.OD),
        (1, const.DN), (1, const.CN), (1, const.HK),
        (1, const.ZT), (1, const.PT), (1, const.HS),
        (1, const.KI), (1, const.ZP), (1, const.LG),
        (1, const.DT), (1, const.VN), (1, const.CR),
        (1, const.MI), (1, const.KR), (1, const.SU),
        (1, const.LV), (1, const.CS), (1, const.HM),
        (1, const.VL), (1, const.RV), (1, const.IF),
        (1, const.TE), (1, const.ZK), (1, const.CZ),
    )

    marka = models.CharField(
        max_length=20,
        null=True,
        default=None,
        verbose_name='Марка автомобіля')

    model = models.CharField(
        max_length=20,
        null=True,
        default=None,
        verbose_name='Модель автомобіля')

    veh_type = models.ForeignKey(
        VehicleType,
        blank=True,
        null=True,
        default=None,
        verbose_name='Тип автомобіля')

    year = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Рік випуску')

    price = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Ціна')

    mileage = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=0,
        verbose_name='Пробіг')

    color = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        default=None,
        verbose_name='Колір')

    fuel = models.CharField(
        max_length=1,
        choices=FUEL_CHOICES,
        blank=False,
        verbose_name='Тип пального')

    capacity = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        blank=True,
        null=True,
        default=None,
        verbose_name="Об'єм двигуна"
    )

    description = models.TextField(
        blank=True,
        null=True,
        default=None,
        verbose_name='Опис')

    location = models.PositiveIntegerField(
        default=0,
        blank=False,
        choices=LOCATION_CHOICES,
        verbose_name='Розташування')

    flag = models.BooleanField(default=True, verbose_name='Act/Deact')

    def __str__(self):
        return "%s %s" % (self.marka, self.model)

    class Meta:
        verbose_name = 'Автомобіль'
        verbose_name_plural = 'Автомобілі'


class VehicleImage(models.Model):
    img = models.ImageField(upload_to='vehicle_image/')
    vehicle = models.ForeignKey(Vehicle, blank=True, null=True, default=None)
    flag = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фото т/з'
        verbose_name_plural = 'Фото т/з'
