from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Book, Transaction, Library

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'isbn')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'created', 'user_id', 'book_id', 'library_id', 'due_date')

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('id', 'name')