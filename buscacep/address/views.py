from django.shortcuts import render
from django.http import HttpResponse
from .models import Address


def home(request):
    context = {
        'addresses': Address.objects.all(),
        'title': 'Listagem',
    }
    return render(request, 'address/home.html', context)


def register(request):
    return render(request, 'address/register.html', {'title': 'Cadastro'})
