import shutil
from django.db import models
from photoshoots.models import Album
import os
from portfolio.utility import generate_path, generate_path_dir
from django.dispatch import receiver
from PhotographSite.settings import MEDIA_DIR


class Image(models.Model):
    """Класс, отвечающий за хранение фотографий"""
    alt = models.CharField(max_length=50, verbose_name="тег <alt>", blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=generate_path)

    def __str__(self):
        return os.path.basename(self.image.path)

    def name(self):
        return str(self)

    def get_url(self):
        return self.image.url


@receiver(models.signals.post_delete, sender=Album)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """ Удаление папки с файлами, при удалении альбома"""
    try:
        path = generate_path_dir(instance.name, "")
        path = os.path.join(MEDIA_DIR, path)
        shutil.rmtree(path)
    except:
        pass


@receiver(models.signals.post_delete, sender=Image)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


class Categories(models.Model):
    """Класс, который содержит информацию о категориях фотографий, выводимых на главной странице"""
    name = models.CharField(max_length=50, verbose_name="Имя категории")
    main_image = models.ForeignKey(Image, on_delete=models.RESTRICT)
    list_of_image = models.ForeignKey(Album, on_delete=models.RESTRICT)

    def get_images(self):
        return Image.objects.filter(album=self.list_of_image)


def get_selected_img(photoshoot):
    obj = Image.objects.filter(album=photoshoot.linkAlbum)
    obj.filter(choosen=True)
    return obj
