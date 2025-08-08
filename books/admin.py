from django.contrib import admin
from .models import Books

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','quantity','created_at']
    search_fields = ['id','title','author','created_at']
    ordering = ['-created_at']
    list_filter = ['author', 'created_at']
    prepopulated_fields = {"slug": ("title",)}