from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.models import User
from users.models import Profile
from django.db.utils import IntegrityError
from users.forms import ProfileForm, SignupForm
from django.views.generic import DetailView
from django.urls import reverse
from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class UserDetailView(LoginRequiredMixin, DetailView):
    """Vista para renderizar detalles de un usuario

    Args:
        DetailView (hernecia): Hereda de DatailView
        Return: renderia una vista
    """
    queryset = User.objects.all()
    slug_field = 'username'  # ? <slug_field> variable unica para encontrar un usuario
    # ? <slug_url_kwarg > toma de la variable de la url debe tener el mismo nombre
    slug_url_kwarg = 'username'
    template_name = 'users/detail.html'

    # ? defino el nombre del contexto
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """añade los posts del usuario al contexto

        Returns:
            [type]: [description]
        """
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


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
            url = reverse('users:detail', kwargs={
                          'username': request.user.username})
            return redirect(url)
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

        user = authenticate(request, username=username,
                            password=password)

        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()

    return render(request, 'users/signup.html',
                  {
                      'form': form
                  })
