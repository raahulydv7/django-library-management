from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,CustomAuthenticationForm,UserProfileForm
from .models import CustomUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

def authenticate_user(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request, 'Login successful.')
            return redirect('root')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()
    return render(request,'users/authenticate_user.html',{'form':form})

def logout_user(request):
    logout(request)
    messages.success(request, "User logged out successfully.")
    return redirect('authenticate')

@login_required
def view_update_user_profile(request):
    profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, "Can't update profile, try again!")

    else:
        form = UserProfileForm(instance=profile)
    
    return render(request,'users/user_profile.html',{'form':form,'profile':profile})
    
