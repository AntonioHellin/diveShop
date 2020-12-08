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

    def __str__(self):
        return 'The name of the article is %s, the section is %s and the price is %s' % (self.name, self.section, self.price)

class Orders(models.Model):

    number = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()