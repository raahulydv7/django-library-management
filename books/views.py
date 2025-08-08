from django.shortcuts import render, redirect,get_object_or_404
from .models import Books,BorrowBook,BookBorrowHistory
from .forms import BookForm,BorrowBookForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils import timezone



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
            return redirect('books')
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

@login_required
def borrow_book(request,slug):
    user = request.user
    book = get_object_or_404(Books, slug=slug)
    if book.quantity <=0:
        messages.error(request, 'This book is currently out of stock')
        return redirect('book-details', book.slug)

    if BorrowBook.objects.filter(user=user, book=book, returned=False).exists():
        messages.warning(request, 'You have already borrowed this book')
        return redirect('book-details', book.slug)

    if request.method == "POST":
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            borrow = form.save(commit=False)
            borrow.user = user
            borrow.book = book
            borrow.save()

            book.quantity -= 1
            book.save()

            BookBorrowHistory.objects.create(
                book_borrow=borrow,
                action='BORROWED',
                note='Book borrowed successfully.'
            ) #create history

            messages.success(request, f"You have successfully borrowed '{book.title}'. Due date: {borrow.due_date}")
            return redirect('book-details', slug=book.slug)
    else:
        form = BorrowBookForm()

    return render(request,'books/borrow_book.html', {'form': form, 'book': book})

@login_required
def borrow_book_history(request):
    user = request.user
    history = BookBorrowHistory.objects.filter(book_borrow__user=user).select_related('book_borrow__book')
    return render(request, 'books/history.html', {'history': history})

@login_required
def return_book(request,borrow_id):
    user = request.user
    borrow = get_object_or_404(BorrowBook, id=borrow_id,user=user)
    borrow.returned = True
    borrow.return_date = timezone.now().date()
    borrow.save()

    BookBorrowHistory.objects.create(
        book_borrow=borrow,
        action='RETURNED',
        note='Book returned successfully.'
    )
    borrow.book.quantity +=1
    borrow.book.save()
    return redirect('history')