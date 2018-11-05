from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView
from .models import Blog


class BlogView(ListView):
    model = Blog
    template_name = 'blog/blogs_list.html'