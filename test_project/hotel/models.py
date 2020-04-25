from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username + " - " + str(self.hotel)


class Hotel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RoomCategory(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    min_price = models.IntegerField()

    def __str__(self):
        return str(self.hotel) + " - " + self.name + " - " + str(self.min_price)

    class Meta:
        verbose_name_plural = 'Room categories'


class Room(models.Model):
    room_category = models.ForeignKey('RoomCategory', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.room_category.hotel) + " - " + str(self.name)


class Booking(models.Model):
    room = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    date_check_in = models.DateTimeField()
    date_check_out = models.DateTimeField()

    def __str__(self):
        return str(self.room)

