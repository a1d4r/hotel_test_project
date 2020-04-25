from django.urls import path
from . import views
from .serializers import *

urlpatterns = [
    path('', views.index_page, name='index'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('change-password/', views.change_password_page, name='change_password'),
    path('api/', views.api_overview, name='api_overview'),
    path('api/hotels/', views.hotel_list, name='api_hotel_list'),
    path('api/user/<int:pk>', views.user_details, name='api_user')
]
