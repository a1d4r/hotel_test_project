from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

urlpatterns = [
    path('', views.index_page, name='index'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('change-password/', views.change_password_page, name='change_password'),
]
