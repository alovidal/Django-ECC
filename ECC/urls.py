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
    path('login', views.login, name='login'),
    path('crud', views.crud, name='crud'),
    path('add_user', views.add_user, name='add_user'),
    path('update_user', views.update_user, name='update_user'),
]