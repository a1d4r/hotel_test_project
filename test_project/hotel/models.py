from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True)


class Hotel(models.Model):
    name = models.CharField(max_length=100)


class RoomCategory(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    min_price = models.IntegerField()


class Room(models.Model):
    room_category = models.ForeignKey('RoomCategory', on_delete=models.SET_NULL, null=True)


class Booking(models.Model):
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    date_check_in = models.DateTimeField()
    date_check_out = models.DateTimeField()

