from django.shortcuts import render
from Auto.models import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from Auto.models import Vehicle
from .forms import VehicleForm

def main(request):
    vehicle_images = VehicleImage.objects.filter(flag=True)
    return render(request, 'main.html', locals())


def vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    return render(request, 'vehpage.html', locals())


def new_vehicle(request):
    """Створюємо новий т/з"""
    if request.method != 'POST':  # Данні юзер не відправив,робимо нову форму
        form = VehicleForm()
    else:
        form = VehicleForm(request.POST)
        if form.is_valid():  # Перевірка на правильність заповнення полів
            form.save()  # Зберігаємо форму в БД
            return HttpResponseRedirect(reverse('main'))  # Перенаправляємо Юзера на вказаний урл
    return render(request, 'new_vehicle.html', locals())