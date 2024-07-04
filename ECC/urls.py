#from django.conf.urls import url 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ranking', views.ranking, name='ranking'),
    path('peleadores', views.peleadores, name='peleadores'),
    path('tienda', views.tienda, name='tienda'),
    path('carro', views.carro, name='carro'),
    path('registro', views.registro, name='registro'),
    path('live', views.live, name='live'),
    
]