from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        'Group',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )


class Group(models.Model):
    title = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="Название группы"
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="Адрес группы"
    )
    description = models.TextField(verbose_name="Описание группы")

    def __str__(self):
        return self.title
