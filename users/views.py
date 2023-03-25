from django.shortcuts import render,redirect
from .forms import customRegistrationForm
from .forms import ProfileForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def register(request):
    #register_form = UserCreationForm()
    #return render(request,'register.html',{'register_form':register_form})
    if request.method=="POST":
        register_form = customRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New User Account Is Created!! Login to get started!!"))
            return redirect('login')
    else:
        register_form = customRegistrationForm()
    return render(request,'register.html',{'register_form':register_form})

def user_data(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form' : form}
    return render(request,"user_form.html",context)

def profile(request):
    return render(request, 'profile.html') 