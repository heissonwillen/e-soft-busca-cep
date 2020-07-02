from django.shortcuts import render
from django.http import HttpResponse


addresses = [
    {
        'cep': '123123123',
        'street': 'Rua Exemplo',
        'number': '123',
        'neighborhood': 'Bairro Exemplo',
        'city': 'Cidade Exemplo',
        'uf': 'Sao Paulo',
        'description': 'Descricão Descricão Descricão Descricão Descricão Descricão ',
        'complement': 'Complemento'
    },
    {
        'cep': '123123123',
        'street': 'Rua Exemplo',
        'number': '123',
        'neighborhood': 'Bairro Exemplo',
        'city': 'Cidade Exemplo',
        'uf': 'Sao Paulo',
        'description': 'Descricão Descricão Descricão Descricão Descricão Descricão ',
        'complement': 'Complemento'
    },
    {
        'cep': '123123123',
        'street': 'Rua Exemplo',
        'number': '123',
        'neighborhood': 'Bairro Exemplo',
        'city': 'Cidade Exemplo',
        'uf': 'Sao Paulo',
        'description': 'Descricão Descricão Descricão Descricão Descricão Descricão ',
        'complement': 'Complemento'
    },
    {
        'cep': '123123123',
        'street': 'Rua Exemplo',
        'number': '123',
        'neighborhood': 'Bairro Exemplo',
        'city': 'Cidade Exemplo',
        'uf': 'Sao Paulo',
        'description': 'Descricão Descricão Descricão Descricão Descricão Descricão ',
        'complement': 'Complemento'
    },
    {
        'cep': '123123123',
        'street': 'Rua Exemplo',
        'number': '123',
        'neighborhood': 'Bairro Exemplo',
        'city': 'Cidade Exemplo',
        'uf': 'Sao Paulo',
        'description': 'Descricão Descricão Descricão Descricão Descricão Descricão ',
        'complement': 'Complemento'
    },
    {
        'cep': '123123123',
        'street': 'Rua Exemplo',
        'number': '123',
        'neighborhood': 'Bairro Exemplo',
        'city': 'Cidade Exemplo',
        'uf': 'Sao Paulo',
        'description': 'Descricão Descricão Descricão Descricão Descricão Descricão ',
        'complement': 'Complemento'
    },
]


def home(request):
    context = {
        'addresses': addresses,
        'title': 'Listagem',
    }
    return render(request, 'address/home.html', context)


def register(request):
    return render(request, 'address/register.html', {'title': 'Cadastro'})
