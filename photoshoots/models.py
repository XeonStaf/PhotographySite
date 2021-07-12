from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class MyUser(User):
   class Meta:
      proxy = True

   def __str__(self):
        return self.first_name + " " + self.last_name

class photo_shoot(models.Model):
    """Класс, в котором храниться данные о фотосессии"""
    States = [
        (6, "Создание мудборда"),
        (5, "Съемка назачена"),
        (4, "Отбор"),
        (3, "Обработка"),
        (2, "Завершено"),
        (1, "Отправлено")
    ]

    name = models.CharField(max_length = 50, verbose_name = "Название фотосессии")
    state = models.IntegerField(
        choices = States,
        default = 6,
        verbose_name = "Статус"
    )
    date = models.DateField(verbose_name = "Дата съемки")
#    moodboard =
    link_to_pinterest = models.URLField(max_length = 200, verbose_name = "Ссылка на доску в Pinterest")
    result_link = models.URLField(max_length = 200, verbose_name = "Ссылка на результат")
    num_choose = models.IntegerField(default = 10, verbose_name="Колличество снимков, котороые нужно выбрать")
    choosen = models.BooleanField(verbose_name = "Снимки уже выбраны", help_text = "Отметить, когда клиент уже отобрал снимки")
    linkUser = models.ForeignKey(MyUser, on_delete = models.RESTRICT)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo-detail', args=[str(self.name)])

