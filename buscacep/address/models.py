from django.db import models

# Create your models here.

class Address(models.Model):
    cep = models.CharField(max_length=9)
    street = models.TextField()
    number = models.CharField(max_length=10)
    neighborhood = models.TextField()
    city = models.TextField()
    uf = models.TextField()
    description = models.TextField()
    complement = models.TextField()

    def __str__(self):
        return f'{self.cep} - {self.street}'
