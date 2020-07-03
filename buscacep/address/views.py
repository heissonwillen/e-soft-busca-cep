from django.shortcuts import render
from django.http import HttpResponse
from .models import Address

from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import ListView, CreateView

from .forms import AddressForm



def home(request):
    context = {
        'addresses': Address.objects.all(),
        'title': 'Listagem',
    }
    return render(request, 'address/home.html', context)


class AddressListView(ListView):
    model = Address
    template_name = 'address/home.html'
    context_object_name = 'addresses'
    paginate_by = 2


class AddressCreateView(CreateView):
    model = Address
    fields = [
        'cep',
        'street',
        'number',
        'neighborhood',
        'city',
        'uf',
        'description',
        'complement'
    ]

    def form_valid(self, form):
        return super().form_valid(form)





# class AddressFormView(FormView):
#     form_class = AddressForm
#     success_url = reverse_lazy('adresses:address')
#     template_name = 'address/register.html'


def register(request):
    return render(request, 'address/register.html', {'title': 'Cadastro'})
