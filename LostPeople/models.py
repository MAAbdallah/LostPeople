from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

class Missed(models.Model) :
    #id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50 , default='undefined')
    Img = models.ImageField(default='default.png', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    Phone_Founder = models.IntegerField(default=0)
    #Phone_Founder = models.PhoneNumberField(null=False , blank=False,unique=True)
    Name_Founder = models.CharField(max_length=50)
    Accept = models.BooleanField(default=False)
    age = models.IntegerField(default=1 , validators=[MinValueValidator(1)])

class Comments(models.Model) :
    #id = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=500 , default='undefined')
    date = models.DateTimeField(auto_now_add=True)
    Auther = models.CharField(max_length=50)
    idCard = models.IntegerField(default=-1)
