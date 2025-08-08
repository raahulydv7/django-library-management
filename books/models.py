from django.db import models
from django.utils.text import slugify
from users.models import CustomUser
from django.utils import timezone
from datetime import timedelta
class Books(models.Model):
    title = models.CharField(max_length=50,unique=True)
    slug = models.CharField(max_length=50, unique=True , blank=True)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="book_images/")
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug =  slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_quantity(self):
        return self.quantity
    
    def __str__(self):
        return f"{self.title} {self.author}"

class BorrowBook(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="borrowed_books")
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="borrow_records")
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    returned = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title} on {self.borrow_date}"

    def is_overdue(self):
        return not self.returned and timezone.now().date() > self.due_date

    def fine_amount(self, fine_per_day=10):
        if self.is_overdue():
            days_overdue = (timezone.now().date() - self.due_date).days
            return days_overdue * fine_per_day
        return 0
    
    def save(self,*args, **kwargs ):
        if not self.due_date:
            self.due_date = timezone.now().date() + timedelta(days=7)
        super().save(*args, **kwargs)

class BookBorrowHistory(models.Model):
    book_borrow = models.ForeignKey(BorrowBook, on_delete=models.CASCADE, related_name="history_records")
    action = models.CharField(max_length=20,choices=[
            ('BORROWED', 'Borrowed'),
            ('RETURNED', 'Returned'),
            ('OVERDUE', 'Overdue')
        ])
    note = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    choices=[
            ('BORROWED', 'Borrowed'),
            ('RETURNED', 'Returned'),
            ('OVERDUE', 'Overdue')
        ]

    def __str__(self):
        return f"History - {self.book_borrow.book.title} ({self.action})"
