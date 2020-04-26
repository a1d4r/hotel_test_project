from django.urls import path
from . import views


urlpatterns = [
    # API detail
    path('', views.api_detail, name='detail'),
    # Users
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('users/', views.user_list, name='user_list'),
    # Hotels
    path('hotels/<int:hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('hotels/', views.hotel_list, name='hotel_list'),
    # Rooms
    path('hotels/<int:hotel_id>/rooms/<int:room_id>/', views.hotel_room_detail, name='hotel_room_detail'),
    path('hotels/<int:hotel_id>/rooms/', views.hotel_room_list, name='hotel_room_list'),
    path('hotels/<int:hotel_id>/room-categories/<int:room_category_id>/rooms/',
         views.category_room_list, name='category_room_list'),
    # Room categories
    path('hotels/<int:hotel_id>/room-categories/<int:room_category_id>/',
         views.room_category_detail, name='room_category_detail'),
    path('hotels/<int:hotel_id>/room-categories/', views.room_category_list, name='room_category_list'),
    # Bookings
    path('hotels/<int:hotel_id>/bookings/<int:booking_id>/', views.hotel_booking_detail, name='hotel_booking_detail'),
    path('hotels/<int:hotel_id>/bookings/', views.hotel_booking_list, name='hotel_booking_list'),
    path('hotels/<int:hotel_id>/rooms/<int:room_id>/bookings/', views.room_booking_list, name='room_booking_list'),
]














