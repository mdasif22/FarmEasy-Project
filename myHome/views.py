from django.shortcuts import render, redirect
from .models import Product,Sell_Product
from users.models import Profile
from .forms import CropForm
from django.contrib import messages
from django.contrib.auth.models import User, auth

def index(request):
    return render(request, 'myHome/index.html')

def cart_products(request):
    user_obj = Profile.objects.get(user=request.user)
    products = Product.objects.filter(owner=user_obj)
    context = {'products':products} 
    return  render(request,'myHome/cart.html',context)

def sell_product_view(request):
    form = CropForm()
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form' : form}
    return render(request,"myHome/sell_form.html",context)

def buy(request):
    user_obj = Profile.objects.get(user=request.user)
    crops = Sell_Product.objects.filter(crop_owner=user_obj)
    context = {'crops':crops} 
    return  render(request,'myHome/Buy.html',context)

def about(request):
    return render(request, 'myhome/about.html')

def contact(request):
   return render(request, 'myhome/contact.html')  

def blog(request):
    return render(request, 'myhome/blog.html')    

def serve(request):
   return render(request, 'myhome/services.html') 

def sell(request):
   return render(request, 'myhome/sell.html')        
    
def cart(request):
    return render(request, 'myhome/cart.html')    

def single_crop(request):
    user_obj = Profile.objects.get(user=request.user)
    crop = Sell_Product.objects.get(id=2)
    context = {'crop':crop} 
    return  render(request,'myHome/product.html',context)
    
