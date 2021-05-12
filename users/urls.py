from django.urls import path
from users import views
from django.views.generic import TemplateView


urlpatterns = [

    # * POSTS
    path(
        route='profile/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    # * MANAGEMENT
    path(
        route='user/login/',
        view=views.login_view,
        name='login'
    ),

    path(
        route='user/logout/',
        view=views.logout_view,
        name='logout'
    ),

    path(
        route='user/signup/',
        view=views.signup_view,
        name='signup'
    ),

    path(
        route='user/me/profile/',
        view=views.update_profile,
        name='update_profile'
    )
]
