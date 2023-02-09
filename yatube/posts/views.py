from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    intro = "Это главная страница проекта Yatube"
    context = {
        "intro": intro
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_posts.html'
    intro = "Здесь будет информация о группах проекта Yatube"
    context = {
        "intro": intro,
    }
    return render(request, template, context)


def group_list(request):
    template = 'posts/group_list.html'
    intro = "Список групп проекта"
    context = {
        "intro": intro,
    }
    return render(request, template, context)

# Create your views here.
