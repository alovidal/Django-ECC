from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'pages/index.html')

def ranking(request):
    return render(request, 'pages/ranking.html')

def peleadores(request):
    return render(request, 'pages/peleadores.html')

def tienda(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'pages/tienda.html', context)

def carro(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create()
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order}
    return render(request, 'pages/carro.html', context)

def registro(request):
    return render(request, 'pages/registro.html')

def live(request):
    return render(request, 'pages/live.html')

def login(request):
    return render(request, 'pages/login.html')

def crud(request):
    return render(request, 'pages/crud.html')

def add_user(request):
    return render(request, 'pages/add_user.html')

def update_user(request):
    return render(request, 'pages/update_user.html')