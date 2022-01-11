from .models import photo_shoot, Review
from django.views import generic
from portfolio.models import Image
import random
from django.http import JsonResponse
from django.contrib.auth.mixins import PermissionRequiredMixin
from photoshoots.utility import permission
from .forms import ReviewForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.templatetags.static import static


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
        if all_photo.count() == 0:
            result = static('/images/home.jpg')
        else:
            result = random.choice(all_photo.all()).get_url()

        context['title'] = "Выбор Фото - " + context['object'].name
        context['right_text'] = 'Выбрано <span class="count"></span> из ' + str(
            context['object'].num_choose) + ' снимков'
        context['main_photo'] = result
        context['menu'] = menu
        context['allPhoto'] = all_photo
        context['special_file'] = True
        return context


PhotoShootsDetail = PhotoShootsDetailView.as_view()


def like_action(request):
    if request.method == "POST" and request.is_ajax():
        obj = photo_shoot.objects.get(id=request.POST['photoshoot_id'])
        if request.user == obj.linkUser and obj.state == 4:
            count = obj.like_photo(request.POST['action'], request.POST['name'])
            return JsonResponse({'count': count, 'name': request.POST['name'], 'step': request.POST['action']},
                                status=200)

    return JsonResponse({}, status=501)


def confirm(request):
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


def review_new(request, pk):
    form = ReviewForm()
    menu = [
        ("bi-house", "portfolio"),
        ("bi-person-square", "personal-area")
    ]
    if request.user == photo_shoot.objects.get(pk=pk).linkUser:
        return render(request, 'photoshoots/review_detail.html',
                      context={
                          'form': form,
                          'navbar_show': True,
                          'title': "Обратная связь",
                          'right_text': "Обратная связь",
                          'menu': menu,
                          'photoshoot_id': pk
                      })
    else:
        return redirect('/')


def confirm_review(request):
    if request.method == "POST" and request.is_ajax():
        photoshoots = photo_shoot.objects.get(pk=request.POST['pk'])
        if request.user == photoshoots.linkUser:
            if Review.objects.filter(photo_shoot=photoshoots).exists():
                return JsonResponse(
                    {'error': "Вы уже оставляли отзыв на эту фотосессию, но вы можете написать мне лично=)"},
                    status=502)
            items = request.POST['content'].split('&')
            data = {}

            for item in items:
                content = item.split('=')
                if content[0].find("csrfmiddlewaretoken") == -1:
                    if content[0].find("post_photo_in_social") != -1:
                        if content[1] == "unknown":
                            data[content[0]] = None
                        else:
                            data[content[0]] = bool(content[1])
                    else:
                        data[content[0]] = content[1]
            result = Review(photo_shoot=photoshoots, **data)
            result.save()
            return JsonResponse({'error': "All is ok"}, status=200)

    return JsonResponse({'error': "Что-то пошло не так...Отзыв не сохранен, пожалуйста, напишите мне"}, status=501)
