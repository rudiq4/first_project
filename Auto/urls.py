from django.conf.urls import url
from Auto import views
from Auto.views import e_handler404, e_handler500

handler404 = e_handler404
handler500 = e_handler500


urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^vehicle/(?P<vehicle_id>\w+)/$', views.vehicle, name='vehicle'),
    url(r'^new_vehicle/$', views.new_vehicle, name='new_vehicle'),
]