from django.shortcuts import render, redirect
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class PostDatailView(DetailView):
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class PostFeedView(LoginRequiredMixin, ListView):
    """Retorna los post con paginación

    Args:
        LoginRequiredMixin ([type]): [description]
        ListView ([type]): [description]

    Returns:
        [type]: [description]
    """
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create new post

    Args:
        login_required ([type]): [description]
        CreateView ([type]): [description]

    Returns:
        [type]: [description]
    """

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["profile"] = self.request.user.profile
        return context
