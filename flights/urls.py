from django.shortcuts import render
from django.conf.urls import url
from . import views



app_name = 'flights' 

urlpatterns = [
    url(r'^$', views.flights_list, name='flight_list'),
    url(r'^new/$', views.flight_new, name='flight_new'),  
    url(r'^(?P<id>\d+)/detail/$', views.flights_details, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', views.flight_update, name='edit'),  
    url(r'^(?P<id>\d+)/delete/$', views.flight_delete, name='flight_delete'),
]

#url(r'^(?P<pk>\d+)/edit/$', views.FlightUpdate.as_view(), name='flight_edit'),  
#url(r'^(?P<pk>\d+)/delete/$', views.FlightDelete.as_view(), name='flight_delete'),
#url(r'', views.FlightList.as_view(), name='flight_list'), 
