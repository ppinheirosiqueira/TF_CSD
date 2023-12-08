from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('controlador/<str:nome>', views.controlador, name="controlador"),
]