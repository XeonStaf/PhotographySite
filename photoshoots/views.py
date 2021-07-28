from .models import photo_shoot
from django.views import generic
from portfolio.models import Image
import random
from django.http import JsonResponse
from django.contrib.auth.mixins import PermissionRequiredMixin
from photoshoots.utility import permission


class PhotoShootsDetailView(PermissionRequiredMixin, generic.DetailView):
    """Страничка, где клиент выбирает фотографии, которые ему понравились"""
    model = photo_shoot

    def has_permission(self):
        obj = photo_shoot.objects.get(pk=self.kwargs['pk'])
        return permission(obj, self.request)

    def get_context_data(self, **kwargs):
        menu = [
            ("bi-house", "portfolio"),
            ("bi-person-square", "personal-area")
        ]
        # Генерация случайной фотографии из серии на обложку
        context = super().get_context_data(**kwargs)
        all_photo = Image.objects.filter(album=context['object'].linkAlbum)
        result = random.choice(all_photo.all()).get_url()

        context['main_photo'] = result
        context['menu'] = menu
        context['allPhoto'] = all_photo
        context['title'] = "Выбор Фото - " + context['object'].name
        context['right_text'] = 'Выбрано <span class="count"></span> из '+ str(context['object'].num_choose) +' снимков'
        context['special_file'] = True
        return context


PhotoShootsDetail = PhotoShootsDetailView.as_view()


def LikeAction(request):

    if request.method == "POST" and request.is_ajax():
        obj = photo_shoot.objects.get(id=request.POST['photoshoot_id'])
        if request.user == obj.linkUser and obj.state == 4:
            count = obj.like_photo(request.POST['action'], request.POST['name'])
            return JsonResponse({'count': count, 'name': request.POST['name'], 'step': request.POST['action']}, status=200)

    return JsonResponse({}, status=501)


def Confirm(request):

    if request.method == "POST" and request.is_ajax():

        obj = photo_shoot.objects.get(id=request.POST['photoshoot_id'])
        if request.user == obj.linkUser:
            obj.comment = request.POST['comment']
            obj.save()
            if len(obj.chosen) <= obj.num_choose and obj.state == 4:
                obj.state = 3
                obj.save()
                return JsonResponse({}, status=200)

    return JsonResponse({'error': "Too many Photos"}, status=501)

