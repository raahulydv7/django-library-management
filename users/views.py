from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def root(request):
    return render(request,'users/root.html')

def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "User Created and logged in!!")
            return redirect('root')
        else:
            messages.success(request, "Unable to create user. Please correct the errors below.")

    else:
        form = CustomUserCreationForm()
    return render(request,'users/create_user.html',{'form':form})

