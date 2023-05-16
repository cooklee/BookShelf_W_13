from django.shortcuts import render
from django.views.generic import ListView

from ksiazki.models import Book, Author


# Create your views here.

class BookGenericListView(ListView):
    model = Book
    template_name = 'list_view.html'

class AuthorGenericListView(ListView):
    model = Author
    template_name = 'list_view.html'
