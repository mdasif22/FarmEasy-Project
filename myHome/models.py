from django.db import models
from users.models import Profile
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(blank=True, null=True)
    quantity = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.product_name)
    
class Sell_Product(models.Model):
    crop_owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    crop_name = models.CharField(max_length=200,null=True,blank=True)
    crop_quan = models.IntegerField(blank=True, null=True)
    crop_price = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.crop_name)

 