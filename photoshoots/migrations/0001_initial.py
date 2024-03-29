# Generated by Django 3.2.5 on 2021-07-18 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя Альбома')),
            ],
        ),
        migrations.CreateModel(
            name='photo_shoot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название фотосессии')),
                ('state', models.IntegerField(choices=[(1, 'Отправлено'), (2, 'Обработка'), (3, 'Выбрано'), (4, 'Необходимо Выбрать'), (5, 'Съемка назачена'), (6, 'Создание мудборда')], default=6, verbose_name='Статус')),
                ('date', models.DateField(verbose_name='Дата съемки')),
                ('moodboard', models.FileField(upload_to='media/moodboard')),
                ('link_to_pinterest', models.URLField(verbose_name='Ссылка на доску в Pinterest')),
                ('result_link', models.URLField(verbose_name='Ссылка на результат')),
                ('num_choose', models.IntegerField(default=10, verbose_name='Колличество снимков, котороые нужно выбрать')),
                ('linkAlbum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photoshoots.album')),
            ],
        ),
    ]
