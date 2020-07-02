from django.db import models

# Create your models here.

class Address(models.Model):
    cep = models.CharField(max_length=8)
    street = models.TextField()
    number = models.CharField(max_length=10)
    neighborhood = models.TextField()
    city = models.TextField()
    uf = models.CharField(max_length=2)
    description = models.TextField()
    complement = models.TextField()

    def __str__(self):
        print(f'{self.cep} - {self.street}')
