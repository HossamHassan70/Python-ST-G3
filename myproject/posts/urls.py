
from django.urls import path
from posts.views import sayhello, welcome, welcome_user, homeuser, profileview , \
indexposts, showpost, allposts, post_detail

urlpatterns = [
    path('mmmmmm', sayhello, name='sayhello'),
    path('welcome', welcome, name='welcome'),
    path('welcomeuser/<name>', welcome_user, name='welcomeuser'),
    path('home/<int:id>', homeuser, name='homeuser'),
    path('profile', profileview, name='profileview'),
    path('', indexposts, name='indexposts'),
    path('<int:id>', showpost, name='showpostname'),
    path('all/', allposts, name='allposts'),
    path('all/<int:id>', post_detail, name='post_detail'),
    
]
