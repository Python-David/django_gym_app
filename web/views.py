from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'web/home.html')


def member_login(request):
    return render(request, 'web/member_login.html')


def trainer_login(request):
    return render(request, 'web/trainer_login.html')


def register(request):
    return render(request, 'web/register.html')


def contact(request):
    return render(request, 'web/contact.html')
