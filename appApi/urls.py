from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inmuebles', views.inmueble_list, name='inmueble list'),
    path('inmueble/<str:pk>', views.detail_inmueble, name='inmueble'),
    path('inmueble-update/<str:pk>', views.update_inmueble, name='update inmueble'),
    path('inmueble-delete/<str:pk>', views.delete_inmueble, name='delete inmueble'),
]
