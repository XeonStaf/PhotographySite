from django.shortcuts import render
from .models import photo_shoot
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num = photo_shoot.objects.all().count()
    num_work = photo_shoot.objects.filter(state__exact=2).count()

    return render(
        request,
        'index.html',
        context={'num' : num, 'num_work' : num_work},
    )

class PhotoSetByUserListView(LoginRequiredMixin, generic.ListView):
    model = photo_shoot
    template_name = 'photoshoots/users_photosets.html'
    paginate_by = 10

    def get_queryset(self):
        return photo_shoot.objects.filter(linkUser = self.request.user)