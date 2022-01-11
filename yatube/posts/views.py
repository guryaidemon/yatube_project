from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    """Главная страница."""

    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        'posts': posts,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


def group_posts(request, slug):
    """Страница группы"""
    
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    # Функция get_object_or_404 получает по заданным критериям объект
    # из базы данных или возвращает сообщение об ошибке, если объект не найден.
    # В нашем случае в переменную group будут переданы объекты модели Group,
    # поле slug у которых соответствует значению slug в запросе
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    # Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    # Словарь с данными принято называть context
    context = {
        # В словарь можно передать переменную
        'title': title,
        'posts': posts,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)
