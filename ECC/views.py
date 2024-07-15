from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

def login(request):
    return render(request, 'pages/registration/login.html')


def index(request):
    context = {
        "user": "",
    }
    return render(request, 'pages/index.html', context)

@login_required

def ranking(request):
    peleadores = Peleador.objects.all()
    context = {'peleadores': peleadores}
    return render(request, 'pages/ranking.html', context)

def peleadores(request):
    peleadores = Peleador.objects.all()
    context = {'peleadores': peleadores}
    return render(request, 'pages/peleadores.html', context)

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

def live(request):
    return render(request, 'pages/live.html')

def live(request):
    return render(request, 'pages/live.html')

def crud(request):
    usuarios = Usuario.objects.all()    
    context = {'usuarios': usuarios}
    return render(request, 'pages/admin/crud.html', context)

def add_user(request):
    usuarios = Usuario.objects.all()    
    context = {'usuarios': usuarios}
    return render(request, 'pages/admin/add_user.html', context)

def update_user(request):
    usuarios = Usuario.objects.all()    
    context = {'usuarios': usuarios}
    return render(request, 'pages/admin/update_user.html', context)