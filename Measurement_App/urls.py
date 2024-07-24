from django.urls import path
from . import views

urlpatterns = [
    path('', views.measurement_show)
] 
