from django.urls import path
from posts import views


urlpatterns = [
    path(
        route='',
        view=views.PostFeedView.as_view(),
        name='feed'
    ),

    path(
        route='posts/new/',
        view=views.CreatePostView.as_view(),
        name='add_post'
    ),

    path(
        route='posts/<int:pk>/',
        view=views.PostDatailView.as_view(),
        name='detail'
    ),


]
