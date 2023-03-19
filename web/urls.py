from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="web_home"),
    path('member_login/', views.member_login, name="web_member_login"),
    path('trainer_login/', views.trainer_login, name="web_trainer_login"),
    path('register/', views.register, name="web_register"),
    path('contact/', views.contact, name="web_contact"),
]
