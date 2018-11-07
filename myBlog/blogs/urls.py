from django.contrib import admin
from django.urls import path, include
from .views import BlogView, Subscribe, Unsubscribe

urlpatterns = [
    path('', BlogView.as_view(), name='blogs_list'),
    path('subscribe/<int:pk>/', Subscribe.as_view(), name='blog_subscribe'),
    path('unsubscribe/<int:pk>/', Unsubscribe.as_view(), name='blog_unsubscribe'),
]