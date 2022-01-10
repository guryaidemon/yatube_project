from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """Главная страница."""

    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


def group_posts(request):
    """Страница группы"""
    
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)
