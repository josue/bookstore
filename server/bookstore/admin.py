from django.contrib import admin
from .models import Book, Transaction, Library

admin.site.register([Book, Transaction, Library])