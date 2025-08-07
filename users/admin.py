from django.contrib import admin
from .models import CustomUser,UserProfile

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'role', 'created_at']
    search_fields = ['id', 'username', 'email']
    ordering = ['-created_at']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'fname','lname' ,'created_at']
    search_fields = ['id', 'user__username','fname','lname']
    ordering = ['-created_at']

    def username(self, obj):
        return obj.user.username