from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Hotel
from .serializers import *


@login_required(login_url='login')
def index_page(request):
    return render(request, 'hotel/index.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('index')
        else:
            messages.error(request, 'Incorrect username or password!')
            return redirect('login')

    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'hotel/login.html', context)


@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def change_password_page(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'The old password is incorrect or new passwords do not match')

    form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'hotel/change_password.html', context)


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




