from django.db import models
from django.contrib.auth.models import User


class MyUser(User):
    """Класс больше нужен для консоли администратора, чтобы выводилось ИФ"""

    class Meta:
        proxy = True

    def __str__(self):
        return self.first_name + " " + self.last_name
