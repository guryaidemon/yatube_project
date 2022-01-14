from django.shortcuts import get_object_or_404, render
from .models import Group, Post

POST_COUNT: int = 10


def index(request):
    """Главная страница."""

    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()[:POST_COUNT]

    context = {
        'title': title,
        'posts': posts,
    }

    return render(request, template, context)


def group_posts(request, slug):
    """Страница группы"""

    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group.title}'
    posts = group.posts.all()[:POST_COUNT]

    context = {
        'title': title,
        'posts': posts,
    }

    return render(request, template, context)
