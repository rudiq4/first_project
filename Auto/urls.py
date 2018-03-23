from django.conf.urls import url
from Auto import views
from Auto.views import e_handler404, e_handler500

handler404 = e_handler404
handler500 = e_handler500

# app_name = 'Auto'

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^vehicle/(?P<vehicle_id>\w+)/$', views.vehicle, name='vehicle'),
    url(r'^new_vehicle/$', views.new_vehicle, name='new_vehicle'),
    url(r'^search-form/$', views.search_form, name='search_form'),
    url(r'^search/$', views.search, name='search'),
    url(r'^testpage/$', views.testpage, name='testpage'),
]