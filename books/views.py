from django.shortcuts import render, redirect,get_object_or_404
from .models import Books
from .forms import BookForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

def root(request):
    return render(request,'books/root.html')


def is_admin(user):
    return user.is_authenticated and user.role == 'ADMIN'

@login_required
@user_passes_test(is_admin, login_url='root')
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully.")
        else:
            messages.error(request, 'Error while creating book , Try again..')
    else:
        form = BookForm()
    return render(request, 'books/add_books.html',{'form':form})

@login_required
def book_list(request):
    books_list = Books.objects.all()
    return render(request, 'books/books_list.html',{'books':books_list})

@login_required
def book_details(request,slug):
    book = get_object_or_404(Books, slug=slug)
    return render(request, 'books/book_details.html',{'book':book})