from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView

from ksiazki.forms import AddBookForm
from ksiazki.models import Book, Author


# Create your views here.

class BookGenericListView(ListView):
    model = Book
    template_name = 'list_view.html'


class UpdateBookView(UpdateView):
    model = Book
    template_name = 'form.html'
    fields = '__all__'


class AddBookGeneric(CreateView):
    model = Book
    form_class = AddBookForm
    template_name = 'form.html'


class AuthorGenericListView(ListView):
    model = Author
    template_name = 'list_view.html'
