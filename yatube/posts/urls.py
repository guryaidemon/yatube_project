# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('group_list/', views.group_posts, name='group_list'),
]
