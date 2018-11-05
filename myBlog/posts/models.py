from django.db import models
from django.contrib.auth.models import User
from blogs.models import Blog


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
