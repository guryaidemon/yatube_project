from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """Главная страница."""

    template = 'posts/index.html'
    return render(request, template)


def group_posts(request):
    """Страница группы"""
    
    template = 'posts/group_list.html'
    return render(request, template)
