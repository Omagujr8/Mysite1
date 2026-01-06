from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('books/add/', add_book, name='add_book'),
]
