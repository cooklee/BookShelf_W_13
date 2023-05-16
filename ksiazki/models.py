from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=128)

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

class Book(models.Model):
    title = models.CharField(max_length=128)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField()


    def __str__(self):
        return self.title
