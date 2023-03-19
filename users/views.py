from django.shortcuts import render


def member_login(request):
    return render(request, 'users/member_login.html')


def register(request):
    return render(request, 'users/register.html')


def trainer_login(request):
    return render(request, 'users/trainer_login.html')
