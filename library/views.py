from django.http import JsonResponse
from .models import Book
from django.shortcuts import render


def get_books(request):
    books = Books.objects.all().values()
    return JsonResponse(books, safe=False)

def home(request):
    return render(request, 'library/home.html')