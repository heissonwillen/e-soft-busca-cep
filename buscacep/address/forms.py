from django import forms


class AddressForm(forms.Form):
    cep = forms.CharField(label='CEP', max_length=9)
    street = forms.CharField(label='Rua', max_length=100)
    number = forms.CharField(label='Número', max_length=10)
    neighborhood = forms.CharField(label='Bairro', max_length=100)
    city = forms.CharField(label='Cidade', max_length=100)
    uf = forms.CharField(label='UF', max_length=100)
    description = forms.CharField(label='Descricão')
    complement = forms.CharField(label='Complemento', max_length=100)
