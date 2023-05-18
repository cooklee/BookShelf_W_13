from datetime import datetime

import pytest

from ksiazki.models import Publisher, Category, Author


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