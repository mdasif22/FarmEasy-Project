from django.db import models
from users.models import Profile
from django.contrib.auth.models import User
import uuid


    
class Sell_Product(models.Model):
    crop_owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    crop_name = models.CharField(max_length=200,null=True,blank=True)
    crop_quan = models.IntegerField(blank=True, null=True)
    crop_price = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.crop_name)

class Cart(models.Model):
    current_user = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    cart_obj = models.ForeignKey(Sell_Product,null=True,blank=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return str(self.cart_obj)
 
class Worker_portal(models.Model):
     name = models.CharField(max_length=200,null=True,blank=True)
     phone = models.IntegerField(null=True,blank=True)
     email = models.EmailField(max_length=200,null=True,blank=True)
     location = models.CharField(max_length=200,null=True,blank=True)
     
     def __str__(self):
        return str(self.name)
    
    
# class Cart(models.Model):
#     cart_owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
#     cart_obj = models.CharField(max_length=200,null=True,blank=True)
    
#     def __str__(self):
#         return str(self.cart_owner)


class User_to_Farmeasy(models.Model):
    crop_owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    crop_name = models.CharField(max_length=200,null=True,blank=True)
    crop_quantity = models.IntegerField(blank=True, null=True)
    crop_price = models.IntegerField(null=True,blank=True)
    approved = models.BooleanField('Approved', default=False)

    def __str__(self):
        return str(self.crop_name)