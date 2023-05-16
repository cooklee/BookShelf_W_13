from django.shortcuts import render
from django.views.generic import ListView

from ksiazki.models import Book


# Create your views here.

class BookGenericListView(ListView):
    model = Book
    template_name = 'list_view.html'
