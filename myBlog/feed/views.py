from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.db.models import Q
from posts.models import Post


class Feed(LoginRequiredMixin, ListView):
    template_name = 'feed/feed_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(
            Q(blog__in=self.request.user.subscriptions.all()) | Q(blog=self.request.user.blog)
        ).all()


class MarkAsRead(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        if request.user not in post.readers.all():
            post.readers.add(request.user)
        return redirect(reverse('feed:feed'))


class MarkAsUnread(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        if request.user in post.readers.all():
            post.readers.remove(request.user)
        return redirect(reverse('feed:feed'))
