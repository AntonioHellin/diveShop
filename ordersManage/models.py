from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Clients(models.Model):

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = CharField(max_length=9)

class Articles(models.Model):

    name = models.CharField(max_length=30)
    section = models.CharField(max_length=20)
    price = models.FloatField()

class Orders(models.Model):

    number = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()