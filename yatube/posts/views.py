from django.http import HttpResponse


def index(request):
    """Главная страница."""
    
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    """Страница группы"""
    
    return HttpResponse(f'Страница группы {slug}')
