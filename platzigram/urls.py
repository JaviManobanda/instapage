"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin  # ? Importa el admin
from django.conf.urls.static import static  # ? Para tere url estaticos
from django.conf import settings  # ? Importando settings
from platzigram import views as localViews
from posts import views as postsViews
from users import views as users_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', localViews.hello_world, name='hello_world'),
    path('sort_integers/', localViews.sort_integers, name='sort'),
    path('welcome/<str:name>/<int:age>/', localViews.welcome, name='hi'),
    path('posts/', postsViews.list_posts, name='feed'),
    path('user/login/', users_Views.login_view, name='login'),
    path('user/logout/', users_Views.logout_view, name='logout'),
    path('user/signup/', users_Views.signup_view, name='signup'),
    path('user/me/profile/', users_Views.update_profile, name='update_profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
