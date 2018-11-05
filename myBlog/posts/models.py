from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from time import time


# Create your models here.

# def gen_slug(s):
#     new_slug = slugify(s, allow_unicode=True)
#     return new_slug + '-' + str(int(time()))


# class Blog(models.Model):
#     """
#     pass
#     """
#     owner = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
#     name = models.CharField(max_length=255, default='Personal Blog')
#     subscribers = models.ManyToManyField(User, related_name='subscriptions', blank=True)
#
#     def __str__(self):
#         return self.name
#
#
# @receiver(post_save, sender=User)
# def create_user_blog(sender, instance, created, **kwargs):
#     if created:
#         Blog.objects.create(owner=instance)
#

class Post(models.Model):
    # blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    title = models.CharField('Заголовок', max_length=150, db_index=True)
    text = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField('Время создания', auto_now_add=True)
    readers = models.ManyToManyField(User, verbose_name='Кто прочитал', blank=True)

    # def get_absolute_url(self):
    #     return reverse('post_detail', kwargs={'slug': self.slug})

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.slug = gen_slug(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-date_pub',)
