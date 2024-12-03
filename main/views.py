from django.shortcuts import render




def dashboard(request):
    return render(request,'dashboard.html')


def books_in_store(request):
    return render(request,'books_in_store.html')


def borrowed(request):
    return render(request, 'borrowed_books.html')


def fines(request):
    return render(request, 'book_fines.html')


def issue(request):
    return None