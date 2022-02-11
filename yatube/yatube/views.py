from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
   template = 'index.html'
   return render(request, template)



def group_posts(request):
   template = 'group_list.html'
   return render(request, template)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def post(request, any_slag):
    return HttpResponse(f'Пост: {any_slag}')