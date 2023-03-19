from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="web_home"),
    path('contact/', views.contact, name="web_contact"),
]
