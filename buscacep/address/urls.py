from django.urls import path, include
# from .views import AddressCreateView
# from .forms import AddressCreateForm
from . import views

urlpatterns = [
    path('', views.home, name='address-home'),
    # path('register/', AddressCreateView.as_view(),  name='address-register'),
    # path('register/', views.register,  name='address-register'),
    path('register/', views.AddressFormView.as_view(),  name='address-register'),
    path('create/', views.create, name='address-create'),
]
