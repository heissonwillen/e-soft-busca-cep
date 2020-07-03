from django.shortcuts import render, redirect
from .models import Address
from django.urls import reverse_lazy

from django.views.generic import FormView
from .forms import AddressForm


def home(request):
    context = {
        'addresses': Address.objects.all(),
    }
    return render(request, 'address/home.html', context)


def create(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            if not Address.objects.filter(cep=form.cleaned_data['cep']):
                a = Address.objects.create(
                    cep = form.cleaned_data['cep'],
                    street = form.cleaned_data['street'],
                    number = form.cleaned_data['number'],
                    neighborhood = form.cleaned_data['neighborhood'],
                    city = form.cleaned_data['city'],
                    uf = form.cleaned_data['uf'],
                    description = form.cleaned_data['description'],
                    complement = form.cleaned_data['complement']
                )
            else:
                Address.objects.filter(cep=form.cleaned_data['cep']).update(
                    street = form.cleaned_data['street'],
                    number = form.cleaned_data['number'],
                    neighborhood = form.cleaned_data['neighborhood'],
                    city = form.cleaned_data['city'],
                    uf = form.cleaned_data['uf'],
                    description = form.cleaned_data['description'],
                    complement = form.cleaned_data['complement']
                )
            return redirect('address-home')
    else:
        form = AddressForm()
    return render(request, 'address/register.html', {'form': form})


class AddressFormView(FormView):
    form_class = AddressForm
    success_url = reverse_lazy('address-home')
    template_name = 'address/register.html'
