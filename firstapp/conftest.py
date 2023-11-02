import pytest
from django.contrib.auth.models import User
from first.models import Sport, Hall, Event, Comment, Like, Dislike



@pytest.fixture
def user():
    user = User.objects.create_user(username='testuser', password='testpassword')
    return user

@pytest.fixture
def sport():
    sport = Sport.objects.create(name='test_sport', description='test_description')
    return sport

@pytest.fixture
def hall():
    hall = Hall.objects.create(name='test_hall', address='test_address')
    return hall

@pytest.fixture
def event(hall, sport, user):
    event = Event.objects.create(owner=user, name='test_event', description='test_description', hall=hall, sport=sport, price=100, date='2023-11-01')
    event.users.add(user)
    return event

@pytest.fixture
def comment(event, user):
    comment = Comment.objects.create(event=event, user=user, text='test_comment')
    return comment

@pytest.fixture
def like(event, user):
    like = Like.objects.create(event=event, user=user)
    return like

@pytest.fixture
def dislike(event, user):
    dislike = Dislike.objects.create(event=event, user=user)
    return dislike
