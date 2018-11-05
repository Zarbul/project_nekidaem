from django.contrib import admin
from django.urls import path, include
from .views import BlogView

urlpatterns = [
    path('', BlogView.as_view(), name='blogs_list'),
]