from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'role', 'created_at']
    search_fields = ['id', 'username', 'email']
    ordering = ['-created_at']