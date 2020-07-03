from django.urls import path, include
from .views import AddressListView, AddressCreateView
from . import views

urlpatterns = [
    path('', AddressListView.as_view(), name='address-home'),
    path('register/', AddressCreateView.as_view(),  name='address-register'),
]
