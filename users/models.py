from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=500,null=True,blank=True)
    phone = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    pin = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return str(self.name)
