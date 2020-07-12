from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Book, Transaction, Library
from .serializers import UserSerializer, BookSerializer, TransactionSerializer, LibrarySerializer

class UsersView(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class BooksView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class TransactionsView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class LibraryView(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class UserBooksView(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer

    class Meta:
        ordering = ['-due_date']

    def get_queryset(self):
        user_id = int(self.kwargs['user_id'])
        return Transaction.objects.filter(user_id=user_id)

class LibraryBooksView(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        library_id = int(self.kwargs['library_id'])
        return Transaction.objects.filter(library_id=library_id)