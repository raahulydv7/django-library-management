from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('book/<slug:slug>/', views.book_borrow_details, name='book-borrow-details'),
]
