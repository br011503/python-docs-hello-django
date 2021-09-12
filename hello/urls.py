from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [    
    url(r'^$', views.index, name='index'),
    url('enthalpy_control/', views.enthalpy_control, name='enthalpy_control'),
    url('oa_control/', views.oa_control, name='oa_control'),
    url('ahu_optimal_control/', views.ahu_optimal_control, name='ahu_optimal_control'),
]
