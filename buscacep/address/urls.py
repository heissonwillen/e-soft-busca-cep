from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='address-home'),
    path('register/', views.register,  name='address-register'),
]
