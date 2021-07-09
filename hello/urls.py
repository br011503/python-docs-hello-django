from django.urls import path, include
from . import views

urlpatterns = [    
    path('', views.index, name='index'),

    path('', views.hello, name='hello'),
]
