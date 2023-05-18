from datetime import datetime

import pytest
from django.contrib.auth.models import User, Permission

from ksiazki.models import Publisher, Category, Author, Book


@pytest.fixture
def wydawcy():
    lst = []
    lst.append(Publisher.objects.create(name='ala'))
    lst.append(Publisher.objects.create(name='gosia'))
    lst.append(Publisher.objects.create(name='kasia'))
    return lst

@pytest.fixture
def kategorie():
    lst = []
    lst.append(Category.objects.create(name='ala'))
    lst.append(Category.objects.create(name='gosia'))
    lst.append(Category.objects.create(name='kasia'))
    return lst


@pytest.fixture
def author():
    a = Author.objects.create(first_name="Slawek", last_name='bo', birth_date=datetime(1990, 12,12))
    return a

@pytest.fixture
def book(author, wydawcy, kategorie):
    b= Book.objects.create(
        author=author,
        publisher=wydawcy[0],
        title = 'Gumisie',
        year = 1233

    )
    b.categories.set(kategorie)
    return b


@pytest.fixture
def user():
    u = User.objects.create(username='gumis')
    return u

@pytest.fixture
def user_with_permission():
    u = User.objects.create(username='gumis')
    perm = Permission.objects.get(codename='view_book')
    u.user_permissions.add(perm)
    return u