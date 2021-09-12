from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [    
    url(r'^$', views.index, name='index'),
    url('enthalpy_control/', views.enthalpy_control, name='enthalpy_control'),
    url('oa_control/', views.oa_control, name='oa_control'),
    url('ahu_optimal_control/', views.ahu_optimal_control, name='ahu_optimal_control'),
    url('elec_consumption/', views.elec_consumption, name='elec_consumption'),
    url('elec_peak/', views.elec_peak, name='elec_peak'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
