from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.models import User
from users.models import Profile
from django.db.utils import IntegrityError
from users.forms import ProfileForm
# Create your views here.


@login_required
def update_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        # ! Aqui el FILE es para el archivo
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.pictureUser = data['picture']
            profile.save()
            return redirect('update_profile')
    else:
        form = ProfileForm()

    return render(request=request,
                  template_name='users/update_profile.html',
                  context={
                      'profile': profile,
                      'user': request.user,
                      'form': form
                  })


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
