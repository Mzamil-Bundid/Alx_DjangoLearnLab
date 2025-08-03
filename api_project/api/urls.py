from django.urls import path
from .views import BookList

     # URL pattern using BookList.as_view
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]