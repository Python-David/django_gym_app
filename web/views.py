from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'web/home.html')


def contact(request):
    return render(request, 'web/contact.html')
