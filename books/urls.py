from django.urls import path
from . import views

urlpatterns = [
    path('root/', views.root, name='root'),
    path('add/',views.add_book, name='add-book'),
    path('',views.book_list, name='books'),
    path('<slug:slug>/',views.book_details, name='book-details'),
]
