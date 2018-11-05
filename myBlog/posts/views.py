from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm


class PostView(ListView):
    model = Post
    template_name = 'post/post_list.html'


class PostCreate(CreateView):
    form_class = PostForm
    template_name = 'posts/post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        # после того как добавим Блог и пользователей
        # blog_article.blog = self.request.user.blog
        post.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('posts_list', args=[self.request.user.blog.pk])