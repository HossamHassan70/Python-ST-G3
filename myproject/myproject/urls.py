"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from posts.views import sayhello, welcome, welcome_user, homeuser, profileview , \
indexposts, showpost
from contactus.views import contactusview

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('mmmmmm', sayhello, name='sayhello'),
    # path('welcome', welcome, name='welcome'),
    # path('welcomeuser/<name>', welcome_user, name='welcomeuser'),
    # path('home/<int:id>', homeuser, name='homeuser'),
    # path('profile', profileview),
    path('contact', contactusview, name='customname'),
    # path('posts', indexposts, name='indexposts'),
    # path('posts/<int:id>', showpost, name='showpostname')
    path('posts/', include('posts.urls'))
    
    
]
