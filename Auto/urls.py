from django.conf.urls import url
from Auto import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^vehicle/(?P<vehicle_id>\w+)/$', views.vehicle, name='vehicle'),
]