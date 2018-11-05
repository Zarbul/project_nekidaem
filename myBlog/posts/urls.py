from django.urls import path
from .views import PostView, PostCreate, PostDetail

urlpatterns = [
    path('', PostView.as_view(), name='posts_list'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]
