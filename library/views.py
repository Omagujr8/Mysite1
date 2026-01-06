from django.http import JsonResponse
from .models import Book
from django.shortcuts import render


def get_books(request):
    books = Books.objects.all().values()
    return JsonResponse(books, safe=False)

def home(request):
    return render(request, 'library/home.html',{
                      'name': 'Junior',
                      'books': ['Harry Potter', 'Python 101', 'CS50 Notes']
                  }
 )

def book_list(request):
    books = Book.objects.all()  # ORM: READ from DB
    return render(request, 'library/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            tittle=request.POST['title'],
            author=request.POST['author'],
            year=request.POST['year'],
            pages=request.POST['pages']
        )
        return redirect("book_list")
    return render(request, 'library/add_book.html')
