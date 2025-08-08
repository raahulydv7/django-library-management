from django.db import models
from django.utils.text import slugify
from users.models import CustomUser
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

