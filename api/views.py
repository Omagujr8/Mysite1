from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser


class IsAdminRole(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
    
class BookAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):

    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        book.delete()
        return Response(status=204)   

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = User.objects.create_user(username=username, password=password)
    return Response({"message": "User created successfully"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": "You are logged in!"})

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminRole])
def admin_dashboard(request):
    return Response({"message": "Admin only"})

@api_view(['GET'])
@permission_classes([IsAdminUser])
def admin_only(request):
    return Response({"message": "Only admin can see this"})