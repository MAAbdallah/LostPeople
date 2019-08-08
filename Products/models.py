from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

class Charity(models.Model) :
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50 , default='undefined')
    address = models.CharField(max_length=100)
    Phone_nubmer = models.IntegerField(default=0)


class Product(models.Model) :
    #id = models.IntegerField(primary_key=True)
    Img = models.ImageField(default='default.jpg', blank=True)
    nameP = models.CharField(max_length=50 , default='undefined')
    Store_location = models.CharField(max_length=100)
    Store_Name = models.CharField(default='storeName',max_length=100)
    price = models.IntegerField(default=0 ,  validators=[MinValueValidator(0)])

class BookMarks(models.Model) :
    idUser = models.IntegerField(default=-1)
    idProduct = models.IntegerField(default=-1)
    Fav = models.BooleanField(default=False)
