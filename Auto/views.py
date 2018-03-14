from django.shortcuts import render
from .models import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import VehicleForm
from django.shortcuts import render_to_response
from django.template import RequestContext


def main(request):
    vehicle_images = VehicleImage.objects.filter(flag=True)
    return render(request, 'main.html', locals())


def vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    return render(request, 'shablon.html', locals())


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




def e_handler404(request):
    context = RequestContext(request)
    response = render_to_response('Errors/error404.html', context)
    response.status_code = 404
    return response


def e_handler500(request):
    context = RequestContext(request)
    response = render_to_response('Errors/error500.html', context)
    response.status_code = 500
    return response
