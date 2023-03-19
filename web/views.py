from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'web/home.html')


def login(request):
    return render(request, 'web/login.html')
