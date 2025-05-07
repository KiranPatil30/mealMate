from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=50)


class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    picture = models.URLField(max_length=300)
    cuisine = models.CharField(max_length=200)
    rating = models.FloatField()


class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=400)
    price = models.FloatField()
    vegitarian = models.BooleanField(default= True)
    image = models.URLField(max_length=200,default='https://i.tribune.com.pk/media/images/1590373-biryani-1513939158/1590373-biryani-1513939158.gif')
    restaurant = models.ForeignKey(Restaurant,on_delete= models.CASCADE,related_name='items')