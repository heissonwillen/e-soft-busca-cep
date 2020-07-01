from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='address-home'),
    path('register/', views.register, name='address-register'),
]
