from django.shortcuts import render, HttpResponse


def index_page(request):
    return HttpResponse('Index page')


def login_page(request):
    return HttpResponse('Login page')


def logout_page(request):
    return HttpResponse('Logout page')


def change_password_page(request):
    return HttpResponse('Change password page')
