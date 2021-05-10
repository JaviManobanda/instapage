from django.shortcuts import render, redirect
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required
from posts.models import Post
from datetime import datetime

# Create your views here.


@login_required
def list_posts(request):
    posts = Post.objects.all().order_by('created')
    return render(request, 'posts/feed.html', {'posts': posts})


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
