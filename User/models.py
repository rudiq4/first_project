from django.db import models
from django.contrib.auth.models import User
from core.models.abstract_models import BaseDjangoModel


# class City(models.Model):
#     city = models.CharField(
#         max_length=32,
#         blank=True,
#         null=True,
#         default=None
#     )
#
#     def __str__(self):
#         return "%s" % self.city
#
#     class Meta:
#         verbose_name = 'Місто'
#         verbose_name_plural = 'Міста'
#
#
# class Profile(BaseDjangoModel):
#     user = models.OneToOneField(User)
#     birthdate = models.DateField(
#         blank=True,
#         default=None,
#         null=True
#     )
#
#     city = models.ForeignKey(
#         City,
#         blank=True,
#         null=True,
#         default=None,
#         verbose_name='Тип автомобіля')
#
#     avatar = models.ImageField(upload_to='avatar/')
#
#     class Meta:
#         verbose_name = 'Профіль користувача'
#         verbose_name_plural = 'Профілі користувачів'
#
#     def __str__(self):
#         return "%s" % self.user





