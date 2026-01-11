from django.urls import path
from .views import post_new, post_list # または PostCreateView
from .views import post_new, post_list, home


urlpatterns = [
    path('post/new/', post_new, name='post_new'),
    path('posts/', post_list, name='post_list'),
    path('', home, name='home'),
]






