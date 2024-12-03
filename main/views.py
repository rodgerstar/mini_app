from django.shortcuts import render

from main.models import Book


def dashboard(request):
    return render(request,'dashboard.html')


def books_in_store(request):
    books = Book.objects.all()
    return render(request,'books_in_store.html',{'books':books})


def borrowed_books(request):
    borrowed = Book.objects.all()
    return render(request, 'borrowed_books.html',{'borrowed_items':borrowed})


def fines(request):
    return render(request, 'book_fines.html')


def issue(request):
    return None