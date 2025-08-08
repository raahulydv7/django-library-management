from django.contrib import admin
from .models import Books,BorrowBook,BookBorrowHistory

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','quantity','created_at']
    search_fields = ['id','title','author','created_at']
    ordering = ['-created_at']
    list_filter = ['author', 'created_at']
    prepopulated_fields = {"slug": ("title",)}

@admin.register(BorrowBook)
class BorrowBookAdmin(admin.ModelAdmin):
    list_display = ['id',"user__username","book__title",'created_at']
    search_fields = ['id','created_at']
    ordering = ['-created_at']

@admin.register(BookBorrowHistory)
class BookBorrowHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_username', 'action', 'created_at']
    search_fields = ['id', 'book_borrow__user__username', 'created_at']
    ordering = ['-created_at']

    def get_username(self, obj):
        return obj.book_borrow.user.username
    get_username.short_description = 'User'