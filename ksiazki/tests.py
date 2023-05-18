import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_index():
    client = Client()
    url = reverse('Index')
    response = client.get(url)
    assert response.status_code == 200
