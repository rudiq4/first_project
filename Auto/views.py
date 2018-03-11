from django.shortcuts import render
from Auto.models import *


def main(request):
    vehicle_images = VehicleImage.objects.filter(flag=True)
    return render(request, 'main.html', locals())


def vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    return render(request, 'vehpage.html', locals())
