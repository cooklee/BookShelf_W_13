from django.shortcuts import render
from django.views import View


# Create your views here.
class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class PublisherListView(View):

    def get(self, request):
        return render(request, 'publisher.html')


class AddPublisherView(View):


    def get(self, request):
        return render(request, 'add_publisher.html')
