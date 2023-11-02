import pytest
from django.test import Client
from django.urls import reverse
import os
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstapp.settings")
settings.configure()

def test_index_view():
    client = Client()  # symuluj przeglądarke
    url = reverse('index')  # pobierz url na który masz wejsc
    response = client.get(url)  # wpisz w adres przegladarki symulowanej
    # pobranego url'a
    assert response.status_code == 200  # sprawdzamy czy widok zwrocił kod 200
    assert response.context['date'] == 'dupa na kiju'

@pytest.mark.django_db
def test_index_view():
    client = Client()
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_view_get():
    client = Client()
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_logout_view():
    client = Client()
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_create_user_view_get():
    client = Client()
    url = reverse('create_user')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_sport_view_not_authenticated(client):
    url = reverse('add_sport')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_sport_view_authenticated(authenticated_client):
    url = reverse('add_sport')
    response = authenticated_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_hall_view_not_authenticated(client):
    url = reverse('add_hall')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_hall_view_authenticated(authenticated_client):
    url = reverse('add_hall')
    response = authenticated_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_event_view_not_authenticated(client):
    url = reverse('add_event')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_event_view_authenticated(authenticated_client):
    url = reverse('add_event')
    response = authenticated_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_join_event_view_not_authenticated(client):
    url = reverse('join_event')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_join_event_view_authenticated(authenticated_client):
    url = reverse('join_event')
    response = authenticated_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_event_view_not_authenticated(client, event):
    url = reverse('edit_event', args=(event.id,))
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_edit_event_view_authenticated(authenticated_client, event):
    url = reverse('edit_event', args=(event.id,))
    response = authenticated_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_show_event_view():
    client = Client()
    url = reverse('show_event')
    response = client.get(url)
    assert response.status_code == 200
