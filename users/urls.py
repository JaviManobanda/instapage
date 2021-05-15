from django.urls import path
from users import views
from django.views.generic import TemplateView


urlpatterns = [
    # * MANAGEMENT
    path(
        route='user/login/',
        view=views.LoginView.as_view(),
        name='login'
    ),

    path(
        route='user/logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        route='user/signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),

    path(
        route='user/me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update_profile'
    ),


    # * POSTS
    path(
        route='profile/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

]
