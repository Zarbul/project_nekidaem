from django.db import models
from django.contrib.auth.models import User
from blogs.models import Blog
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    title = models.CharField('Заголовок', max_length=150, db_index=True)
    text = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField('Время создания', auto_now_add=True)
    readers = models.ManyToManyField(User, verbose_name='Кто прочитал', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-date_pub',)


@receiver(post_save, sender=Blog)
def send_notify(sender, instance, created, **kwargs):
    if created:
        for sub in instance.blog.subscribers.all():
            if sub.email:
                send_mail(
                    '{} - new article in {} {}.'.format(instance.title,
                                                        instance.blog.owner.username,
                                                        instance.blog.name),
                    'Link to new article: {}'.format(
                        settings.BASE_URL + reverse('post_detail', args=[instance.pk])),
                    'notify@example.com',
                    [sub.email],
                    fail_silently=False,
                )
