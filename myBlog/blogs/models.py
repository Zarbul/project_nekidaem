from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from time import time
# Create your models here.
class Blog(models.Model):
    """
    pass
    """
    owner = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=255, default='Personal Blog')
    subscribers = models.ManyToManyField(User, related_name='subscriptions', blank=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=User)
def create_user_blog(sender, instance, created, **kwargs):
    if created:
        Blog.objects.create(owner=instance)
