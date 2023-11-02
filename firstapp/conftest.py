import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from first.models import Sport, Hall, Event

@pytest.fixture
def create_user(db):
    def make_user(username='testuser', password='testpassword'):
        return User.objects.create_user(username=username, password=password)
    return make_user

@pytest.fixture
def authenticated_user(client, create_user):
    user = create_user()
    client.login(username=user.username, password='testpassword')
    return user

@pytest.fixture
def create_sport(db):
    def make_sport(name='Test Sport', description='Test Description'):
        return Sport.objects.create(name=name, description=description)
    return make_sport

@pytest.fixture
def create_hall(db):
    def make_hall(name='Test Hall', address='Test Address'):
        return Hall.objects.create(name=name, address=address)
    return make_hall

@pytest.fixture
def create_event(db, create_sport, create_hall):
    def make_event(name='Test Event', description='Test Description'):
        sport = create_sport()
        hall = create_hall()
        return Event.objects.create(name=name, description=description, hall=hall, sport=sport, price=10, date='2023-11-02')
    return make_event
