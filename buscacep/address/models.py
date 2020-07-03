from django.db import models
from django.urls import reverse

# Create your models here.

class Address(models.Model):
    cep = models.CharField(max_length=9)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)
    description = models.TextField()
    complement = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.cep} - {self.street}'

    def get_absolute_url(self):
        return reverse('address-home')
