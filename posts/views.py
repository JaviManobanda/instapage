from django.shortcuts import render, redirect
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required
from posts.models import Post
from datetime import datetime
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


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
    paginate_by = 2
    context_object_name = 'posts'


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()

    return render(request, template_name='posts/new.html',
                  context={
                      'form': PostForm,
                      'user': request.user,
                      'profile': request.user.profile
                  })
