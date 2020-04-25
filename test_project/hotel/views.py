from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


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
