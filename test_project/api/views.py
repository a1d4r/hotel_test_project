from django.shortcuts import render, Http404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from hotel.models import *
from .serializers import *


@api_view(['GET'])
def api_detail(request):
    api_urls = {
        'List hotels': '/hotels/',
    }
    return Response(api_urls)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def hotel_list(request):
    hotels = Hotel.objects.all()
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def user_detail(request, user_id):
    user = get_object_or_404(User.objects.all(), pk=user_id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def room_category_list(request, hotel_id):
    # Return 404 if hotel does not exist
    get_object_or_404(Hotel.objects.all(), pk=hotel_id)

    room_categories = RoomCategory.objects.filter(hotel__id=hotel_id)
    serializer = RoomCategorySerializer(room_categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def hotel_room_list(request, hotel_id):
    # Return 404 if hotel does not exist
    get_object_or_404(Hotel.objects.all(), pk=hotel_id)

    rooms = Room.objects.filter(room_category__hotel__id=hotel_id)
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_room_list(request, hotel_id, room_category_id):
    room_category = get_object_or_404(RoomCategory.objects.all(), pk=room_category_id)
    # if room category is not in the specified hotel
    if room_category.hotel.id != hotel_id:
        raise Http404

    rooms = room_category.room_set.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def hotel_booking_list(request, hotel_id):
    # Return 404 if hotel does not exist
    get_object_or_404(Hotel.objects.all(), pk=hotel_id)

    bookings = Booking.objects.filter(room__room_category__hotel__id=hotel_id)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def room_booking_list(request, hotel_id, room_id):
    room = get_object_or_404(Room.objects.all(), pk=room_id)
    # if room_id is not in the specified hotel
    if room.room_category.hotel.id != hotel_id:
        raise Http404

    bookings = room.booking_set.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)
