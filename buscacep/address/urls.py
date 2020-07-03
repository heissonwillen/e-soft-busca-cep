from django.urls import path, include
# from .views import AddressCreateView
# from .forms import AddressCreateForm
from . import views

urlpatterns = [
    path('list', views.home, name='address-home'),
    # path('register/', AddressCreateView.as_view(),  name='address-register'),
    # path('register/', views.register,  name='address-register'),
    path('', views.AddressFormView.as_view(),  name='address-register'),
    path('create/', views.create, name='address-create'),
]
