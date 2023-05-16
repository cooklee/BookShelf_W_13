from django.shortcuts import render, redirect
from django.views import View

from ksiazki.forms import AddAuthorForm, AddBookForm
from ksiazki.models import Publisher, Category, Author


# Create your views here.
class IndexView(View):

    def get(self, request):
        return render(request, 'base.html', {'pc':Publisher.objects.count()})


class PublisherListView(View):

    def get(self, request):
        publishers = Publisher.objects.order_by('name')
        return render(request, 'publisher.html',
                      {'publishers': publishers, })

class CategoryListView(View):

    def get(self, request):
        category = Category.objects.order_by('name')
        return render(request, 'category.html',
                      {'categories': category})

class AuthorListView(View):

    def get(self, request):
        authors = Author.objects.order_by('last_name', 'first_name')
        return render(request, 'author_list.html',  {'authors': authors})


class AddPublisherView(View):

    def get(self, request):
        return render(request, 'add_publisher.html')

    def post(self, request):
        name = request.POST.get('name', '')
        Publisher.objects.create(name=name)
        return redirect('publisher_list')



class AddCategoryView(View):

    def get(self, request):
        return render(request, 'add_category.html', {'pc':'dupa'})

    def post(self, request):
        name = request.POST.get('name', '')
        Category.objects.create(name=name)
        return redirect('categories_list')


class UpdatePublisherView(View):

    def get(self, request, pk):
        publisher = Publisher.objects.get(pk=pk)
        return render(request, 'add_publisher.html', {'publisher': publisher})

    def post(self, request, pk):
        publisher = Publisher.objects.get(pk=pk)
        name = request.POST.get('name', '')
        publisher.name = name
        publisher.save()
        return redirect('publisher_list')

class UpdateCategoryView(View):

    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        return render(request, 'add_category.html', {'category': category})

    def post(self, request, pk):
        category = Category.objects.get(pk=pk)
        name = request.POST.get('name', '')
        category.name = name
        category.save()
        return redirect('categories_list')

class AddBookView(View):

    def get(self, request):
        form = AddBookForm()
        return render(request, 'add_book.html', {'form':form})

    def post(self, request):
        form = AddBookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('index')
        return render(request, 'add_book.html', {'form': form})

class AddAuthorView(View):

    def get(self, request):
        form = AddAuthorForm()
        return render(request, 'add_author.html', {'form':form})

    def post(self, request):
        form = AddAuthorForm(request.POST) # stworz mi formularz wypełniony danymi które wysłał użytkownik
        if form.is_valid(): #wykonaj walidacje formularza (czyli sprawdz poprawność danych)
            # is_valid jesli dana jest poprawna wykonuje rzutowanie na odp typ i zapisuje
            # daną w słowniku cleaned_data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            date = form.cleaned_data['date']
            Author.objects.create(first_name=first_name, last_name=last_name, birth_date=date)
            return redirect('add_author')
        return render(request, 'add_author.html', {'form': form})


class UpdateAuthorView(View):

    def get(self, request, pk):
        author = Author.objects.get(pk=pk)
        form = AddAuthorForm(initial={'first_name':author.first_name,
                                      'last_name':author.last_name,
                                      'date':author.birth_date})
        return render(request, 'add_author.html', {'form':form})

    def post(self, request, pk):
        author = Author.objects.get(pk=pk)
        form = AddAuthorForm(request.POST) # stworz mi formularz wypełniony danymi które wysłał użytkownik
        if form.is_valid(): #wykonaj walidacje formularza (czyli sprawdz poprawność danych)
            # is_valid jesli dana jest poprawna wykonuje rzutowanie na odp typ i zapisuje
            # daną w słowniku cleaned_data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            date = form.cleaned_data['date']
            author.first_name=first_name
            author.last_name=last_name
            author.birth_date=date
            author.save()
            return redirect('add_author')
        return render(request, 'add_author.html', {'form': form})








