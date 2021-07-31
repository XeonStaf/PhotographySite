# Generated by Django 3.2.5 on 2021-07-18 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('photoshoots', '0002_photo_shoot_linkuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo_shoot',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата съемки'),
        ),
        migrations.AlterField(
            model_name='photo_shoot',
            name='linkAlbum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photoshoots.album', verbose_name='Альбом'),
        ),
        migrations.AlterField(
            model_name='photo_shoot',
            name='linkUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='user.myuser', verbose_name='Герой'),
        ),
        migrations.AlterField(
            model_name='photo_shoot',
            name='link_to_pinterest',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на доску в Pinterest'),
        ),
        migrations.AlterField(
            model_name='photo_shoot',
            name='moodboard',
            field=models.FileField(upload_to='moodboard', verbose_name='Мудборд'),
        ),
        migrations.AlterField(
            model_name='photo_shoot',
            name='result_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на результат'),
        ),
    ]