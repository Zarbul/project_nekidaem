from django.urls import path
from . import views

app_name = 'feed'
urlpatterns = [
    path('post/mark-as-read/<int:pk>/', views.MarkAsRead.as_view(), name='mark_as_read'),
    path('post/mark-as-unread/<int:pk>/', views.MarkAsUnread.as_view(), name='mark_as_unread'),
    path('', views.Feed.as_view(), name='feed')
]
