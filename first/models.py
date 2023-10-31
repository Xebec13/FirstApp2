from django.contrib.auth.models import User
from django.db import models



class Sport(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Hall(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


class Event(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # owner
    name = models.CharField(max_length=100)
    description = models.TextField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    price = models.IntegerField()
    date = models.DateField()
    users = models.ManyToManyField(User, related_name='events', blank=True)


class Guest(models.Model):
    name = models.CharField(max_length=50)


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField()
