from django.urls import path, include
from . import views

urlpatterns = [    
    path('', views.hello, name='index'),
    path('', views.hello, name='hello'),
]
