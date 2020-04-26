from django.shortcuts import render, Http404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .permissions import IsHotelRelated
from hotel.models import *
from .serializers import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_detail(request):
    api_urls = {
        'User list': '/users/',
        'User detail': '/users/<user_id>/',
        'Hotel list': '/hotels/',
        'Hotel detail': '/hotels/<hotel_id>/',
        'Room detail': '/hotels/<hotel_id>/rooms/<room_id>/',
        'Room list': {
            '/hotels/<hotel_id>/rooms/',
            '/hotels/<hotel_id>/room-categories/<room_category_id>/rooms/',
        },
        'Room category detail': '/hotels/<hotel_id>/room-categories/<room_category_id>/',
        'Room category list': '/hotels/<hotel_id>/room-categories/',
        'Booking detail': '/hotels/<hotel_id>/bookings/<booking_id>',
        'Booking list': {
            '/hotels/<hotel_id>/bookings',
            '/hotels/<hotel_id>/rooms/<room_id>/bookings/',
        },
    }
    return Response(api_urls)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def user_detail(request, user_id):
    user = get_object_or_404(User.objects.all(), pk=user_id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser | IsHotelRelated])
def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel.objects.all(), pk=hotel_id)
    serializer = HotelSerializer(hotel, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def hotel_list(request):
    hotels = Hotel.objects.all()
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser | IsHotelRelated])
def hotel_room_detail(request, hotel_id, room_id):
    room = get_object_or_404(Room.objects.all(), pk=room_id)

    # if room is not in the specified hotel
    if room.room_category.hotel.id != hotel_id:
        raise Http404

    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser | IsHotelRelated])
def hotel_room_list(request, hotel_id):
    # Return 404 if hotel does not exist
    get_object_or_404(Hotel.objects.all(), pk=hotel_id)

    rooms = Room.objects.filter(room_category__hotel__id=hotel_id)
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser | IsHotelRelated])
def room_category_detail(request, hotel_id, room_category_id):
    room_category = get_object_or_404(RoomCategory.objects.all(), pk=room_category_id)

    # if room category is not in the specified hotel
    if room_category.hotel.id != hotel_id:
        raise Http404

    serializer = RoomCategorySerializer(room_category, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser | IsHotelRelated])
def room_category_list(request, hotel_id):
    # Return 404 if hotel does not exist
    get_object_or_404(Hotel.objects.all(), pk=hotel_id)

    room_categories = RoomCategory.objects.filter(hotel__id=hotel_id)
    serializer = RoomCategorySerializer(room_categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser | IsHotelRelated])
def category_room_list(request, hotel_id, room_category_id):
    room_category = get_object_or_404(RoomCategory.objects.all(), pk=room_category_id)

    # if room category is not in the specified hotel
    if room_category.hotel.id != hotel_id:
        raise Http404

    rooms = room_category.room_set.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser | IsHotelRelated])
def hotel_booking_detail(request, hotel_id, booking_id):
    booking = get_object_or_404(Booking.objects.all(), pk=booking_id)

    # if booking is not in the specified hotel
    if booking.room.room_category.hotel.id != hotel_id:
        raise Http404

    serializer = BookingSerializer(booking, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser | IsHotelRelated])
def hotel_booking_list(request, hotel_id):
    # Return 404 if hotel does not exist
    get_object_or_404(Hotel.objects.all(), pk=hotel_id)

    bookings = Booking.objects.filter(room__room_category__hotel__id=hotel_id)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser | IsHotelRelated])
def room_booking_list(request, hotel_id, room_id):
    room = get_object_or_404(Room.objects.all(), pk=room_id)
    # if room_id is not in the specified hotel
    if room.room_category.hotel.id != hotel_id:
        raise Http404

    bookings = room.booking_set.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)
