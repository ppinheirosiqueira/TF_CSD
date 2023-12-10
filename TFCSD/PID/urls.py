from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('controlador/<str:nome>', views.controlador, name="controlador"),
    path('atualizarTF/<str:num>/<str:den>/<str:tipo>/<str:kp>/<str:ki>/<str:kd>', views.atualizarTF, name="atualizarTF"),
]