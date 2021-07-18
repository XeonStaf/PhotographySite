from django.shortcuts import render
from .models import Categories
from django.templatetags.static import static

# Create your views here.
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    categories = Categories.objects.all()
    if (request.user.is_authenticated):
        username = request.user.first_name
    else:
        username = "Гость"

    return render(
        request,
        'index.html',
        context={
            'categories' : categories,
            'main_photo' : static('/images/home.jpg'),
            'needed_js_file' : True,
            'right_text' : "Привет, " + username + "!"
        },
    )