from django.shortcuts import render
from .models import Address
from django.shortcuts import redirect
from django.urls import reverse_lazy



from django.views.generic import ListView, CreateView, UpdateView, FormView

from .forms import AddressForm


def home(request):
    context = {
        'addresses': Address.objects.all(),
    }
    return render(request, 'address/home.html', context)


# class AddressCreateView(CreateView):
#     model = Address
#     template_name = 'address/register.html'
#     fields = [
#         'cep',
#         'street',
#         'number',
#         'neighborhood',
#         'city',
#         'uf',
#         'description',
#         'complement'
#     ]
#
#     def form_valid(self, form):
#         print(form)
#         return super().form_valid(form)

# class AddressListView(ListView):
#     model = Address
#     template_name = 'address/home.html'
#     context_object_name = 'addresses'
#     paginate_by = 2


# def register(request):
#     form = AddressForm
#     return render(request, 'address/register.html', {'form': form})

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

        else:
            print(form.errors)
    else:
        form = AddressForm()
    return render(request, 'address/register.html', {'form': form})


class AddressFormView(FormView):
    form_class = AddressForm
    success_url = reverse_lazy('address-home')
    template_name = 'address/register.html'
