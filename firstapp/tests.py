import pytest
from django.urls import reverse
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first.settings')
django.setup()


@pytest.mark.django_db
def test_index_view(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_login_view_get(client):
    response = client.get(reverse('login'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_login_view_post_correct_credentials(client, create_user):
    user = create_user()
    response = client.post(reverse('login'), {'username': user.username, 'password': 'testpassword'})
    assert response.status_code == 302

@pytest.mark.django_db
def test_login_view_post_incorrect_credentials(client, create_user):
    user = create_user()
    response = client.post(reverse('login'), {'username': user.username, 'password': 'incorrectpassword'})
    assert response.status_code == 200

@pytest.mark.django_db
def test_logout_view(client):
    response = client.get(reverse('logout'))
    assert response.status_code == 302

@pytest.mark.django_db
def test_create_user_view_get(client):
    response = client.get(reverse('create'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_user_view_post(client):
    response = client.post(reverse('create'), {'username': 'testuser', 'password': 'testpassword', 'confirm_password': 'testpassword'})
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_sport_view_get(client, authenticated_user):
    response = client.get(reverse('sport'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_sport_view_post(client, authenticated_user):
    response = client.post(reverse('sport'), {'name': 'Test Sport', 'description': 'Test Description'})
    assert response.status_code == 302

@pytest.mark.django_db
def test_add_hall_view_get(client, authenticated_user):
    response = client.get(reverse('hall'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_hall_view_post(client, authenticated_user):
    response = client.post(reverse('hall'), {'name': 'Test Hall', 'address': 'Test Address'})
    assert response.status_code == 302

@pytest.mark.django_db
def test_add_event_view_get(client, authenticated_user):
    response = client.get(reverse('event'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_event_view_post(client, authenticated_user, create_sport, create_hall):
    sport = create_sport()
    hall = create_hall()
    response = client.post(reverse('event'), {'name': 'Test Event', 'description': 'Test Description', 'hall': hall.id, 'sport': sport.id, 'price': 10, 'date': '2023-11-02'})
    assert response.status_code == 302

@pytest.mark.django_db
def test_join_event_view_get(client, authenticated_user):
    response = client.get(reverse('join_event'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_edit_event_view_get(client, authenticated_user, create_event):
    event = create_event()
    response = client.get(reverse('edit_event', kwargs={'event_id': event.id}))
    assert response.status_code == 200

@pytest.mark.django_db
def test_edit_event_view_post(client, authenticated_user, create_event, create_sport, create_hall):
    event = create_event()
    sport = create_sport()
    hall = create_hall()
    response = client.post(reverse('edit_event', kwargs={'event_id': event.id}), {'name': 'Test Event Updated', 'description': 'Test Description Updated', 'hall': hall.id, 'sport': sport.id, 'price': 15, 'date': '2023-11-03'})
    assert response.status_code == 200

@pytest.mark.django_db
def test_delete_event_view_get(client, authenticated_user, create_event):
    event = create_event()
    response = client.get(reverse('delete_event', kwargs={'event_id': event.id}))
    assert response.status_code == 302

@pytest.mark.django_db
def test_add_comment_view_post(client, authenticated_user, create_event):
    event = create_event()
    response = client.post(reverse('add_comment', kwargs={'event_id': event.id}), {'comment_text': 'Test Comment'})
    assert response.status_code == 302

@pytest.mark.django_db
def test_like_event_view_post(client, authenticated_user, create_event):
    event = create_event()
    response = client.post(reverse('like_event', kwargs={'event_id': event.id}))
    assert response.status_code == 302

@pytest.mark.django_db
def test_dislike_event_view_post(client, authenticated_user, create_event):
    event = create_event()
    response = client.post(reverse('dislike_event', kwargs={'event_id': event.id}))
    assert response.status_code == 302

@pytest.mark.django_db
def test_show_event_view(client):
    response = client.get(reverse('show_event'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_edit_event_view_get_unauthenticated(client, create_event):
    event = create_event()
    response = client.get(reverse('edit_event', kwargs={'event_id': event.id}))
    assert response.status_code == 302

@pytest.mark.django_db
def test_delete_event_view_get_unauthenticated(client, create_event):
    event = create_event()
    response = client.get(reverse('delete_event', kwargs={'event_id': event.id}))
    assert response.status_code == 302

@pytest.mark.django_db
def test_add_comment_view_post_unauthenticated(client, create_event):
    event = create_event()
    response = client.post(reverse('add_comment', kwargs={'event_id': event.id}), {'comment_text': 'Test Comment'})
    assert response.status_code == 302

@pytest.mark.django_db
def test_like_event_view_post_unauthenticated(client, create_event):
    event = create_event()
    response = client.post(reverse('like_event', kwargs={'event_id': event.id}))
    assert response.status_code == 302

@pytest.mark.django_db
def test_dislike_event_view_post_unauthenticated(client, create_event):
    event = create_event()
    response = client.post(reverse('dislike_event', kwargs={'event_id': event.id}))
    assert response.status_code == 302

@pytest.mark.django_db
def test_show_event_view_with_no_events(client):
    response = client.get(reverse('show_event'))
    assert response.status_code == 200
