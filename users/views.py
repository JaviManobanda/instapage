from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views  # * Vistas para autentificación
from django.contrib.auth.models import User
from users.models import Profile
from django.db.utils import IntegrityError
from users.forms import SignupForm, ProfileForm
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy
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


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    form_class = ProfileForm
    #fields = ['website', 'biography', 'phone_number', 'pictureUser']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    pass


class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
