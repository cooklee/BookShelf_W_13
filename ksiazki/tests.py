import pytest
from django.test import Client
from django.urls import reverse

from ksiazki.forms import AddBookForm
from ksiazki.models import Publisher, Book, Author


@pytest.mark.django_db
def test_index():
    client = Client()
    url = reverse('Index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_publisher_list(wydawcy):
    client = Client()
    url = reverse('publisher_list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['publishers'].count() == len(wydawcy)
    for p in wydawcy:
        assert p in response.context['publishers']


@pytest.mark.django_db
def test_category_list(kategorie):
    client = Client()
    url = reverse('categories_list')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['categories'].count() == len(kategorie)
    for c in kategorie:
        assert c in response.context['categories']


@pytest.mark.django_db
def test_add_publisher_get():
    client = Client()
    url = reverse('publisher_add')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_publisher_post():
    client = Client()
    url = reverse('publisher_add')
    data = {
        'name': 'ppp'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    redirect_url = reverse('publisher_list')
    assert response.url.startswith(redirect_url)
    Publisher.objects.get(name='ppp')


@pytest.mark.django_db
def test_add_book_get():
    client = Client()
    url = reverse('book_add')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], AddBookForm)


@pytest.mark.django_db
def test_add_book_post(author, wydawcy, kategorie):
    client = Client()
    url = reverse('book_add')
    data = {
        'author': author.id,
        'publisher': wydawcy[0].id,
        'year': 2000,
        'title': 'Gumisie',
        'categories': [c.id for c in kategorie]
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(reverse('book_add'))
    Book.objects.get(title='Gumisie')


@pytest.mark.django_db
def test_add_book_post_year_less_then_b_date(author, wydawcy, kategorie):
    client = Client()
    url = reverse('book_add')
    data = {
        'author': author.id,
        'publisher': wydawcy[0].id,
        'year': 200,
        'title': 'Gumisie',
        'categories': [c.id for c in kategorie]
    }
    response = client.post(url, data)
    assert response.status_code == 200
    try:
        Book.objects.get(title='Gumisie')
        assert False
    except Book.DoesNotExist:
        assert True
    form = response.context['form']
    assert isinstance(form, AddBookForm)
    assert 'Nie mógł napisać tej ksiązki w tym roku' in form.errors['__all__']


@pytest.mark.django_db
def test_update_book_get(book):
    client = Client()
    url = reverse('book_generic_update', kwargs={'pk':book.pk})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_book_post(book):
    client = Client()
    url = reverse('book_generic_update', kwargs={'pk':book.pk})
    autor = Author.objects.get(pk=1)
    wydawca = Publisher.objects.get(pk=1)
    data = {
        'author': autor.id,
        'publisher': wydawca.id,
        'year': 2000,
        'title': 'Gumisie2',
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url.startswith(book.get_absolute_url())
    b = Book.objects.get(title='Gumisie2')
    assert b.id == book.id


@pytest.mark.django_db
def test_book_list_view_not_login(book):
    client = Client()
    url = reverse('book_list')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))

@pytest.mark.django_db
def test_book_list_view_login_without_permission(book, user):
    client = Client()
    client.force_login(user)
    url = reverse('book_list')
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_book_list_view_login_with_permission(book, user_with_permission):
    client = Client()
    client.force_login(user_with_permission)
    url = reverse('book_list')
    response = client.get(url)
    assert response.status_code == 200
