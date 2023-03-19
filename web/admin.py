from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # specify which fields should be displayed in the list view of users
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_member', 'is_trainer', 'is_staff')

    # specify which fields should be used to search for users
    search_fields = ('username', 'email', 'first_name', 'last_name')


admin.site.register(CustomUser, CustomUserAdmin)
