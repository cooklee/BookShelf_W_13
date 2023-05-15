from django.shortcuts import render, redirect
from django.views import View

from ksiazki.models import Publisher, Category


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
