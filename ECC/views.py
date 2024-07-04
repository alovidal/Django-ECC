from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def ranking(request):
    return render(request, 'pages/ranking.html')

def peleadores(request):
    return render(request, 'pages/peleadores.html')

def tienda(request):
    return render(request, 'pages/tienda.html')

def carro(request):
    return render(request, 'pages/carro.html')

def registro(request):
    return render(request, 'pages/registro.html')

def live(request):
    return render(request, 'pages/live.html')