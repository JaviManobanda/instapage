from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.models import User
from users.models import Profile
from django.db.utils import IntegrityError
# Create your views here.


def update_profile(request):
    return render(request, 'users/update_profile.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        user = authenticate(request, username=username,
                            password=password)

        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confi = request.POST['password_confi']

        if password != password_confi:
            return render(request, 'users/signup.html',
                          {'error': 'Password confirmation does not match'})
        else:
            try:
                user = User.objects.create_user(
                    username=username, password=password)
            except IntegrityError:
                return render(request, 'users/signup.html',
                              {'error': 'Username is already in use'})

            user.first_name = request.POST['firstname']
            user.last_name = request.POST['lastname']
            user.email = request.POST['email']
            user.save()
            profile = Profile(user=user)
            profile.save()
            return redirect('login')

    return render(request, 'users/signup.html')
