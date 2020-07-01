from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'address/home.html', {'title': 'Listagem'})


def register(request):
    return render(request, 'address/register.html', {'title': 'Cadastro'})
