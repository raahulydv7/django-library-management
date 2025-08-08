from django.urls import path
from . import views

urlpatterns = [

    path('add/',views.add_book, name='add-book'),
    path('',views.book_list, name='books'),
    path('<slug:slug>/',views.book_details, name='book-details'),
    path('borrow/<slug:slug>/', views.borrow_book, name='borrow-book'),
]
