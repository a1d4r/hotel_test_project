from rest_framework import serializers
from django.contrib.auth.models import User
from hotel.models import *


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RoomCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomCategory
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        validator = []

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        overlapping = Booking.objects.filter(
            date_check_in__lt=data['date_check_out'],
            date_check_out__gt=data['date_check_in'],
            room=data['room']
        )
        if overlapping.exists():
            raise serializers.ValidationError("The time interval overlaps with another one")
        return data
