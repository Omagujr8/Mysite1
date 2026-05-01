from django.urls import path
from .views import BookAPIView, book_detail, register

urlpatterns = [
    path('books/', BookAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', book_detail),
    path('register/', register),
]