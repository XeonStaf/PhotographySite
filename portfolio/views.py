from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов


    return render(
        request,
        'index.html',
        context={},
    )