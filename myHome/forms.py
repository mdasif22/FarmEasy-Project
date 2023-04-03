from django import forms 
from django.forms import ModelForm
from .models import Sell_Product,Worker_portal,User_to_Farmeasy

class CropForm(ModelForm):
    class Meta:
        model = Sell_Product
        #fields = '__all__'
        fields = ['crop_name','crop_quan','crop_price']
        
class WorkerForm(ModelForm):
    class Meta:
        model = Worker_portal
        fields = '__all__'
        #fields = ['crop_name','crop_quan','crop_price']
        

class UserToUsForm(ModelForm):
    class Meta:
        model = User_to_Farmeasy
        fields = ['crop_name','crop_quantity','crop_price']
        
        
        