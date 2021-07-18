from django.db import models
from django.urls import reverse
from photoshoots.utility import States_for_model, States
from user.models import MyUser
# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя Альбома")

    def __str__(self):
        return self.name


class photo_shoot(models.Model):
    """Класс, в котором храниться все данные о фотосессии"""
    """Фотографии храняться в связанном альбоме, есть связь с пользователем"""
    name = models.CharField(max_length = 50, verbose_name = "Название фотосессии")
    state = models.IntegerField(
        choices = States_for_model,
        default = 6,
        verbose_name = "Статус"
    )
    date = models.DateField(verbose_name = "Дата съемки", null=True, blank=True)
    moodboard = models.FileField(upload_to="moodboard", verbose_name="Мудборд")
    link_to_pinterest = models.URLField(max_length = 200, verbose_name = "Ссылка на доску в Pinterest", null=True, blank=True)
    result_link = models.URLField(max_length = 200, verbose_name = "Ссылка на результат", null=True, blank=True)
    num_choose = models.IntegerField(default = 10, verbose_name="Колличество снимков, котороые нужно выбрать")
    linkUser = models.ForeignKey(MyUser, on_delete = models.RESTRICT, verbose_name="Герой")
    linkAlbum = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name="Альбом")

    def get_text_status(self):
        return States[self.state - 1][1]

    def get_color_status(self):
        return States[self.state - 1][2]

    def get_moodboard_url(self):
        return self.moodboard.url

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('choose', args=[str(self.id,)])


