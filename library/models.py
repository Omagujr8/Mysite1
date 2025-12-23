from django import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.IntegerField()
    pages = models.IntegerField()
