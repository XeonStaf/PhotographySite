from django.db import models
from django.urls import reverse
from photoshoots.utility import States_for_model, States
from user.models import MyUser


class Album(models.Model):
    """Модель альбома. В нее загружаются фото, которые соединены с категориями и фотосесессиями"""
    name = models.CharField(max_length=100, verbose_name="Имя Альбома")

    def __str__(self):
        return self.name


class photo_shoot(models.Model):
    """Модель, в котором храниться все данные о фотосессии"""
    """Фотографии храняться в связанном альбоме, есть связь с пользователем"""
    name = models.CharField(max_length=50, verbose_name="Название фотосессии")
    state = models.IntegerField(
        choices=States_for_model,
        default=6,
        verbose_name="Статус"
    )
    date = models.DateField(verbose_name="Дата съемки", null=True, blank=True)
    moodboard = models.FileField(upload_to="moodboard", verbose_name="Мудборд", null=True, blank=True)
    link_to_pinterest = models.URLField(max_length=200, verbose_name="Ссылка на доску в Pinterest", null=True,
                                        blank=True)
    result_link = models.URLField(max_length=200, verbose_name="Ссылка на результат", null=True, blank=True)
    num_choose = models.IntegerField(default=10, verbose_name="Колличество снимков, котороые нужно выбрать")
    linkUser = models.ForeignKey(MyUser, on_delete=models.RESTRICT, verbose_name="Герой")
    linkAlbum = models.ForeignKey(Album, on_delete=models.SET_NULL, verbose_name="Альбом", null=True, blank=True)
    chosen = models.JSONField(default=list, verbose_name="Выбранные фото", blank=True)
    comment = models.CharField(max_length=200, verbose_name="Комментарий", null=True, blank=True)

    class Meta:
        ordering = ['-date', 'state']

    def like_photo(self, action, name):
        data = set(self.chosen)
        if action == '1':
            data.add(name)
        else:
            try:
                data.remove(name)
            except:
                pass

        self.chosen = list(data)
        self.save()
        return len(data)

    def get_text_status(self):
        return States[self.state - 1][1]

    def get_color_status(self):
        return States[self.state - 1][2]

    def get_moodboard_url(self):
        return self.moodboard.url

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('choose', args=[str(self.id, )])

    def get_chosen(self):
        result = []
        for item in self.chosen:
            buf = item.split('.')
            if len(buf) == 2:
                result.append(buf[0])
            else:
                result.append("ERROR at" + item)
        to_return = ""
        for photo in result:
            to_return += photo + ', '

        return to_return[:-2]


class Review(models.Model):
    """Модель отзыва. В ней хранятся вопросы и соединенная фотосессия"""
    photo_shoot = models.ForeignKey(photo_shoot, on_delete=models.RESTRICT)

    # question
    what_liked = models.TextField(null=True, blank=True,
                                  verbose_name="Что вам не очень понравилось? (организация, долго время ожидания фото)")
    what_disliked = models.TextField(null=True, blank=True, verbose_name="Что вам вам понравилось?")
    post_photo_in_social = models.BooleanField(null=True, blank=True,
                                               verbose_name="Выложили ли фото в какие-либо социальные сети?")
    rate_mood = models.IntegerField(
        null=True, blank=True,
        verbose_name="Оцените ваше общее впечаталение после съемки (от 1 до 5)"
    )
    rate_photo = models.IntegerField(
        null=True, blank=True,
        verbose_name="Оцените ваше общее впечатление от фото (от 1 до 5)"
    )
    rate_site_speed = models.IntegerField(
        null=True, blank=True,
        verbose_name="Оцените скорость работы сайта (от 1 до 5)"
    )

    def __str__(self):
        return "Отзыв " + str(self.photo_shoot.__str__())
