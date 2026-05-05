from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.permissions import BasePermission

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published = models.DateField()

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=[
            ('admin', 'Admin'),
            ('user', 'User')
        ],
        default='user'
    )

class IsAdminRole(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'