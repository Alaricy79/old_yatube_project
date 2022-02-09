from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница постов')


def group_posts(request):
    return HttpResponse('Группа')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def post(request, any_slag):
    return HttpResponse(f'Пост: {any_slag}')