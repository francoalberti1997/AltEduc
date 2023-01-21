from django.db import models

# Create your models here.

class Person(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField(max_length=254)
    age = models.IntegerField()

    def __str__(self):
        return self.nombre