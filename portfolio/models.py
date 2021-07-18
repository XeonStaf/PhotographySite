from django.db import models
from photoshoots.models import Album
import os
from portfolio.utility import generate_path


class Image(models.Model):
    """Класс, отвечающий за хранение фотографий"""
    alt = models.CharField(max_length=50, verbose_name="тег <alt>")
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)
    image = models.ImageField(upload_to=generate_path)

    def __str__(self):
        return os.path.basename(self.image.path)

    def get_url(self):
        return self.image.url


class Categories(models.Model):
    """Класс, который содержит информацию о категориях фотографий, выводимых на главной странице"""
    name = models.CharField(max_length=50, verbose_name="Имя категории")
    main_image = models.ForeignKey(Image, on_delete=models.RESTRICT)
    list_of_image = models.ForeignKey(Album, on_delete=models.RESTRICT)

    def get_images(self):
        return Image.objects.filter(album=self.list_of_image)
