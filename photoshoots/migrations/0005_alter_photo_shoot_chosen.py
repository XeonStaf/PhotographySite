# Generated by Django 3.2.5 on 2021-07-22 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoshoots', '0004_auto_20210721_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo_shoot',
            name='chosen',
            field=models.JSONField(blank=True, default='{}', null=True),
        ),
    ]