from django.contrib.auth import get_user_model
from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Transaction(models.Model):
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    due_date = models.DateField()

    class Meta:
        ordering = ['-due_date']