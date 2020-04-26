from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('hotels/', views.hotel_list, name='api_hotel_list'),
    path('user/<int:pk>', views.user_details, name='api_user')
]