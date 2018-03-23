from django.db import models
from . import const  # для областей
from core.models.abstract_models import BaseDjangoModel


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


class Vehicle(BaseDjangoModel):
    FUEL_CHOICES = (
        ('P', 'Бензин'),
        ('D', 'Дизель'),
        ('L', 'Газ/Бензин'),
        ('H', 'Гібрид'),
        ('E', 'Електромобіль')
    )
    LOCATION_CHOICES = (
        (0, "---"),
        (1, const.OD),
        (2, const.DN), (3, const.CN), (4, const.HK),
        (5, const.ZT), (6, const.PT), (7, const.HS),
        (8, const.KI), (9, const.ZP), (10, const.LG),
        (11, const.DT), (12, const.VN), (13, const.CR),
        (14, const.MI), (15, const.KR), (16, const.SU),
        (17, const.LV), (18, const.CS), (19, const.HM),
        (20, const.VL), (21, const.RV), (22, const.IF),
        (23, const.TE), (24, const.ZK), (25, const.CZ),
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
        max_length=2,
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
