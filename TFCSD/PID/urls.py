from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('icons/favicon.ico'))), 
    path('', views.home, name="home"),
    path('controlador/<str:nome>', views.controlador, name="controlador"),
    path('atualizarTF/<str:num>/<str:den>/<str:tipo>/<str:kp>/<str:ki>/<str:kd>', views.atualizarTF, name="atualizarTF"),
]