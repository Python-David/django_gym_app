from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="web-home"),
    path('login/', views.login, name="web-login")
]