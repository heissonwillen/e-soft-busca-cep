from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('<h1>address list</h1>')


def register(request):
    return HttpResponse('<h1>register an address</h1>')
