from django.conf.urls import url,include
from django.contrib import admin
from User import views

app_name = 'User'

urlpatterns = [
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
]