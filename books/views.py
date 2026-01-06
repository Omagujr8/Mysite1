from django.shortcuts import render
from django.http import JsonResponse

def get_books(request):
    return JsonResponse({
        "books": [
            "Django for Beginners",
            "Python Crash Course"
        ]
    })

