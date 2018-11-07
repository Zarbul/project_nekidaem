from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm


class PostView(ListView):
    model = Post
    template_name = 'post/post_list.html'


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'posts/post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.blog = self.request.user.blog
        post.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('posts_list')


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(self.model, pk=kwargs['pk'])
        if request.user not in post.readers.all():
            post.readers.add(request.user)
        return render(request, self.template_name, context={'post': post})
