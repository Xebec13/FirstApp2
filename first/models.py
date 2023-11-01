from django.contrib.auth.models import User
from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Hall(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    price = models.IntegerField()
    date = models.DateField()
    users = models.ManyToManyField(User, related_name='events', blank=True)

class Like(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Dislike(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='dislikes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
