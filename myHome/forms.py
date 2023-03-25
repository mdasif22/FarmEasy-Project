from django import forms 
from django.forms import ModelForm
from .models import Sell_Product

class CropForm(ModelForm):
    class Meta:
        model = Sell_Product
        #fields = '__all__'
        fields = ['crop_name','crop_quan','crop_price']