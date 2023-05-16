from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView

from ksiazki.models import Book, Author


# Create your views here.

class BookGenericListView(ListView):
    model = Book
    template_name = 'list_view.html'

    def get_queryset(self):
        return super().get_queryset().objects.order_by('title')

class UpdateBookView(UpdateView):
    model = Book
    template_name = 'form.html'
    fields = '__all__'



class AddBookGeneric(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'form.html'


class AuthorGenericListView(ListView):
    model = Author
    template_name = 'list_view.html'
