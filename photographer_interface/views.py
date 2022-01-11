from django.shortcuts import render
from .forms import ImageForm
from django.http import JsonResponse
from portfolio.models import Image
from photoshoots.models import Album
from django.shortcuts import redirect
from django.views import generic
from photoshoots.models import PhotoShoot
from django.contrib.auth.mixins import PermissionRequiredMixin


def photo_new(request):
    form = ImageForm()
    menu = [
        ("bi-person-square", "personal-area")
    ]
    if request.user.is_superuser:
        return render(request, 'photographer_interface/upload_files.html',
                      context={
                          'form': form,
                          'navbar_show': True,
                          'title': "Загрузка Фото",
                          'right_text': "Загрузка Фото",
                          'menu': menu,
                      })
    else:
        return redirect('/')


def upload(request):
    if request.method == "POST" and request.user.is_superuser:
        files = request.FILES.getlist('file')
        for f in files:
            upload = Image.objects.create(
                album=Album.objects.get(pk=request.POST['album']),
                image=f,
            )
            print(Album.objects.get(pk=request.POST['album'])),
            print(f)

        return JsonResponse({}, status=200)

    return JsonResponse({'error': "Too many Photos"}, status=501)


class AllPhoto(PermissionRequiredMixin, generic.ListView):
    """Личный кабинет, где перечисляются фотосессии пользователя"""
    model = PhotoShoot
    template_name = 'photographer_interface/all_photos.html'
    paginate_by = 10

    def has_permission(self):
        return self.request.user.is_superuser

    def get_queryset(self):
        return PhotoShoot.objects.all()

    def get_context_data(self, **kwargs):
        menu = [
            ("bi-house", "portfolio")
        ]
        context = super().get_context_data(**kwargs)
        context['right_text'] = context['title'] = 'Все фото'
        context['navbar_show'] = True
        context['menu'] = menu

        return context


all_photo = AllPhoto.as_view()
