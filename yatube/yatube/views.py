from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
   template = 'index.html'
   context={'text':'Главная страница'}
   return render(request, template, context)


def group_posts(request):
   template = 'group_list.html'
   context={'text':'Посты участников'}
   return render(request, template, context)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def post(request, any_slag):
    return HttpResponse(f'Пост: {any_slag}')