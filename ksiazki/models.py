from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=128)

    def get_absolute_url(self):
        return reverse('publisher_update', kwargs={'pk': self.id})

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('author_update', kwargs={'pk': self.pk})


class Book(models.Model):
    title = models.CharField(max_length=128)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=False)
