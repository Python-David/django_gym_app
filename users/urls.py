from django.urls import path
from . import views

urlpatterns = [
    path('member_login/', views.member_login, name="users_member_login"),
    path('trainer_login/', views.trainer_login, name="users_trainer_login"),
    path('register/', views.register, name="users_register"),
]
