from django.contrib import admin
from django.urls import path, include
from .views import PostView, PostCreate

urlpatterns = [
    path('', PostView.as_view(), name='posts_list'),
    path('create/', PostCreate.as_view(), name='post_create'),
]