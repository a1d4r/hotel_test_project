from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from hotel.models import *
from .serializers import *


@api_view(['GET'])
def api_overview(request):
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
def user_details(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)