from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Client(models.Model):

    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    #address = models.CharField(max_length=50, verbose_name = "The address") #To see a different name in the administration panel
    email = models.EmailField(blank = True, null = True)
    phone = CharField(max_length=9)

    def __str__(self):
        return self.name

class Article(models.Model):

    name = models.CharField(max_length=30)
    section = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return 'The name of the article is %s, the section is %s and the price is %s' % (self.name, self.section, self.price)

class Order(models.Model):

    number = models.IntegerField()
    date = models.DateField()
    delivered = models.BooleanField()