from django.shortcuts import render,get_object_or_404,redirect
from users.models import CustomUser
from books.models import Books,BorrowBook
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages


@login_required
def dashboard(request):
    if request.user.role == "ADMIN":
        books = Books.objects.all()
        return render(request, "dashboard/admin_dashboard.html", {"books": books})
    else:
        borrowed_books = BorrowBook.objects.filter(user=request.user)
        return render(request, "dashboard/user_dashboard.html", {"borrowed_books": borrowed_books})


@login_required
def book_borrow_details(request, slug):
    if request.user.role != "ADMIN":
        messages.error(request, "You are not authorized to view this page.")
        return redirect("dashboard")

    book = get_object_or_404(Books, slug=slug)
    borrow_records = BorrowBook.objects.filter(book=book)
    return render(request, "dashboard/book_borrow_details.html", {"book": book, "borrow_records": borrow_records})
        