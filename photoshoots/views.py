from .models import photo_shoot
from django.views import generic
from portfolio.models import Image
import random


class PhotoShootsDetailView(generic.DetailView):
    """Страничка, где клиент выбирает фотографии, которые ему понравились"""
    model = photo_shoot

    def get_context_data(self, **kwargs):
        # Генерация случайной фотографии из серии на обложку
        context = super().get_context_data(**kwargs)
        all_photo = Image.objects.filter(album=context['object'].linkAlbum)
        result = random.choice(all_photo.all()).get_url()
        print(result)
        context['main_photo'] = result
        return context


PhotoShootsDetail = PhotoShootsDetailView.as_view()

