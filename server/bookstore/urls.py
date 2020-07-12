from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UsersView)
router.register('users/(?P<user_id>\d+)/books', views.UserBooksView, basename='Book')
router.register('books', views.BooksView)
router.register('transactions', views.TransactionsView)
router.register('library', views.LibraryView)
router.register('library/(?P<library_id>\d+)/books', views.LibraryBooksView, basename='Library')

urlpatterns = [
    path('', include(router.urls))
]
