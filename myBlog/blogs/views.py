from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, View
from .models import Blog


class BlogView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog/blogs_list.html'


class Subscribe(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=kwargs['pk'])
        if blog.owner != request.user and request.user not in blog.subscribers.all():
            blog.subscribers.add(request.user)
        return redirect(reverse('blogs_list'))


class Unsubscribe(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=kwargs['pk'])
        if blog.owner != request.user and request.user in blog.subscribers.all():
            blog.subscribers.remove(request.user)
        return redirect(reverse('blogs_list'))
