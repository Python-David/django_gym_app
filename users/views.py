from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm


def member_login(request):
    return render(request, 'users/member_login.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and log in the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            messages.success(request, f'Account created for {username}!')
            # user = authenticate(request, username=username, password=password)
            # login(request, user)
            # Redirect to a success page
            return redirect('web_home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {"form": form})


def trainer_login(request):
    return render(request, 'users/trainer_login.html')
